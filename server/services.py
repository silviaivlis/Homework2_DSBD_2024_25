from database import Session, Engine, BaseClass
from database import FinancialData, Users
from threading import Lock
import logging
import requests
import yfinance as yf
import re

BaseClass.metadata.create_all(bind=Engine)

idRequestCache = {}
cache_lock = Lock()

logging.getLogger("yfinance").setLevel(logging.CRITICAL)

def checkConnection():
    try:
        requests.get("https://finance.yahoo.com", timeout=5)
        return True
    except requests.ConnectionError:
        return False


def verifyTicker(ticker):
    if not checkConnection():
        print("Errore di connesione: controlla la tua rete.")
    else:
        data = yf.download(ticker, period="1d", progress=False)
        if data.empty:
            print(f"Verifica del ticker '{ticker}' errata: nessun dato trovato.")
            return False
        else:
            print(f"Verifica del ticker '{ticker}' andata a buon fine. Dato trovato")
            return True


def verifyEmail(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email) is not None

def checkValue(highValue, lowValue):
    if highValue is None and lowValue is None:
        return True
    elif highValue is None or lowValue is None:
        return True
    else:
        return highValue > lowValue


class User_Command_Service:
    @staticmethod
    def handle_register_user(command):
        with cache_lock:
            if command.requestId in idRequestCache:
                logging.warning(f"id {command.requestId} duplicato")
                return idRequestCache[command.requestId]
            
        session = Session()
        if verifyEmail(command.email) and verifyTicker(command.ticker) and checkValue(command.highValue, command.lowValue):
            user = session.query(Users).filter_by(email=command.email).first()
            if user:
                response = {"message":"Errore registrazione: utente già esistente con questa email!"}
            else:
                newUser = Users(email=command.email,ticker=command.ticker,highValue=command.highValue,lowValue=command.lowValue)
                session.add(newUser)
                session.commit()
                response = {"message":"Utente registrato correttamente!"}

            with cache_lock:
                idRequestCache[command.requestId] = response

            return response
        
        print("Formato email non valido")


    @staticmethod
    def handle_update_ticker(command):
        with cache_lock:
            if command.requestId in idRequestCache:
                print(f"id {command.requestId} duplicato")
                return idRequestCache[command.requestId]

        session = Session()
        if verifyEmail(command.email) and verifyTicker(command.ticker):
            user = session.query(Users).filter_by(email=command.email).first()
            if user:
                if user.ticker == command.ticker:
                    response = {"message":"L'utente possiede già questo ticker!"}
                else:
                    user.ticker = command.ticker
                    session.commit()
                    response = {"message":"Utente aggiornato correttamente!"}
            else:
                response = {"message":"Utente non esistente!"}
        
        
            with cache_lock:
                idRequestCache[command.requestId] = response

            return response
        
        print("Formato email non valido")


    @staticmethod
    def handle_update_values(command):
        with cache_lock:
            if command.requestId in idRequestCache:
                print(f"id {command.requestId} duplicato")
                return idRequestCache[command.requestId]

        session = Session()
        if verifyEmail(command.email):
            user = session.query(Users).filter_by(email=command.email).first()
            if user:
                if command.highValue == 0 and command.lowValue == 0:
                    response = {"message":"Valori soglia non modificati!"}
                elif command.highValue != 0 and command.lowValue == 0:
                    if checkValue(command.highValue, user.lowValue):
                        user.highValue = command.highValue
                        session.commit()
                        response = {"message":"Valore soglia massima aggiornato correttamente!"}
                    else:
                        response = {"message":"Valore soglia massima non valido. Risulta minore della soglia minima!"}
                elif command.highValue == 0 and command.lowValue != 0:
                    if checkValue(user.highValue, command.lowValue):
                        user.lowValue = command.lowValue
                        session.commit()
                        response = {"message":"Valore soglia minima aggiornato correttamente!"}
                    else:
                        response = {"message":"Valore soglia minima non valido. Risulta maggiore della soglia massima!"}
                else:
                    if checkValue(command.highValue, command.lowValue):
                        user.highValue = command.highValue
                        user.lowValue = command.lowValue
                        session.commit()
                        response = {"message":"I valori soglia sono stati aggiornati correttamente!"}
                    else:
                        response = {"message":"Errore: la soglia minima è maggiore della soglia massima!"}
            else:
                response = {"message":"Utente non esistente!"}
        
        
            with cache_lock:
                idRequestCache[command.requestId] = response

            return response
        
        print("Formato email non valido")


    @staticmethod
    def handle_delete_user(command):
        with cache_lock:
            if command.requestId in idRequestCache:
                print(f"id {command.requestId} duplicato")
                return idRequestCache[command.requestId]
        
        session = Session()
        if verifyEmail(command.email):
            user = session.query(Users).filter_by(email=command.email).first()

            if user:
                session.delete(user)
                session.commit()
                response = {"message":"Utente eliminato correttamente!"}
            else:
                response = {"message":"Utente non esistente!"}
        
            with cache_lock:
                idRequestCache[command.requestId] = response

            return response
        
        print("Formato email non valido")


class User_Query_Service:
    @staticmethod
    def get_latest_value(command):
        email = command.email

        session = Session()
        if verifyEmail(email):
            user = session.query(Users).filter_by(email=command.email).first()
            if user:
                ticker = user.ticker
                if ticker:
                    latestData = session.query(FinancialData).filter_by(ticker=ticker).order_by(FinancialData.timestamp.desc()).first()

                    if latestData:
                        return {
                            "email": email,
                            "ticker": ticker,
                            "value": latestData.value,
                            "timestamp": latestData.timestamp.isoformat()
                        }
                    else:
                        return {
                            "email": email,
                            "ticker": ticker,
                            "value": None,
                            "timestamp": None
                        }
                #caso ticker non presente
                return {
                    "email":email,
                    "ticker": None,
                    "value": None,
                    "timestamp": None
                }
            #caso utente non esistente
            else:
                return {
                    "email": None,
                    "ticker": None,
                    "value": None,
                    "timestamp": None
                }
        else:
            print("Formato email non valido")

    
    @staticmethod
    def get_avarage_value(command):
        email = command.email
        numValue = command.count

        session = Session()
        if verifyEmail(email):
            user = session.query(Users).filter_by(email=command.email).first()
            if user:
                ticker = (session.query(Users).filter_by(email=command.email).first()).ticker
                if ticker:
                    values = session.query(FinancialData).filter_by(ticker=ticker).order_by(FinancialData.timestamp.desc()).limit(numValue).all()

                    if len(values) > 0:
                        avarageValue = sum([value.value for value in values])/len(values)
                        return {
                            "email": email,
                            "ticker": ticker,
                            "averageValue": avarageValue
                        }
                    else:
                        return {
                                "email": email,
                                "ticker": ticker,
                                "averageValue": None
                        }
                #caso ticker non presente
                return {
                    "email": email,
                    "ticker": None,
                    "averageValue": None
                }
            else:
                #caso utente non esistente
                return {
                    "email": None,
                    "ticker": None,
                    "averageValue": None
                }
        else:
            print("Formato email non valido")
