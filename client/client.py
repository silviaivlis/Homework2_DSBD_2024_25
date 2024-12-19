import re
import logging
import yfinance as yf
import grpc
import random
from proto import op_pb2, op_pb2_grpc
import requests

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


def generateIdRequest(operation, email, ticker=None):
    randNum = random.randint(0, 9999)
    ranNumformatted = f"{randNum:04}"
    uniqueString = "{}{}{}{}".format(operation, email, ticker if ticker else '', ranNumformatted)
    return uniqueString

def checkValue(highValue, lowValue):
    if highValue is None and lowValue is None:
        return True
    elif highValue is None or lowValue is None:
        return True
    else:
        return highValue > lowValue

def run() : 
    print("Eseguo un collegamento con il server!")
    with grpc.insecure_channel('localhost:50051') as channel_command, grpc.insecure_channel('localhost:50052') as channel_query:
        stubCommand = op_pb2_grpc.User_command_serviceStub(channel_command)
        stubQuery = op_pb2_grpc.User_query_serviceStub(channel_query)

        while True:
            print("\n|-------------------------------------------------------|")
            print("\nSeleziona un'operazione:")
            print("1. Registrazione utente")
            print("2. Aggiornamento Ticker")
            print("3. Aggiornamento Valori")
            print("4. Cancellazione utente")
            print("5. Recupero dell'ultimo valore disponibile dell'azione")
            print("6. Calcolare la media degli ultimi X valori dell'azione")
            print("7. Esci")
            print("\n|-------------------------------------------------------|")
            print("\n")
            scelta = input("Inserisci il numero dell'operazione desiderata: ")

            #------------------------------------------------------------FUNZIONE_1
            if scelta == '1':
                print("\n\n|-------- REGISTRAZIONE UTENTE --------|\n")
                while True:
                    email = input("email: ")
                    email_valid = verifyEmail(email)
                    if email_valid:
                        break
                    print("Formato email errato!")
                while True:
                    ticker = input("ticker: ")
                    ticker_valid = verifyTicker(ticker)
                    if ticker_valid:
                        break
                
                while True:
                    while True:
                        sceltaHigh = input("Vuoi inserire un valore di soglia massimo?(y/n) ")
                        if sceltaHigh == "y" or sceltaHigh == "n":
                            if sceltaHigh == "y":
                                highValue = float(input("Inserisci high value: "))
                            else:
                                highValue = None
                                print("Nessun high value impostato")
                            break
                        print("Scelta non valida")
                    
                    while True:
                        sceltaLow = input("Vuoi inserire un valore di soglia minima?(y/n) ")
                        if sceltaLow == "y" or sceltaLow == "n":
                            if sceltaLow == "y":
                                lowValue = float(input("Inserisci low value: "))
                            else:
                                lowValue = None
                                print("Nessun low value impostato")
                            break
                        print("Scelta non valida")

                    if checkValue(highValue,lowValue):
                        break
                    else:
                        print("Errore: la soglia minima è maggiore della soglia massima. Reinserisci i dati")

                if email_valid and ticker_valid:
                    operation = 'RegisterUser'
                    id_Request = generateIdRequest(operation, email)

                    response = stubCommand.RegisterUser(op_pb2.RegUserRequest(
                        email=email, 
                        ticker=ticker,
                        requestId=id_Request,
                        highValue=highValue,
                        lowValue=lowValue
                    ))

                    # implementazione retry
                    # if not response.message.strip():
                    #     print("Retry...")
                    #     response = stub.RegisterUser(op_pb2.RegUserRequest(
                    #     email=email, 
                    #     ticker=ticker,
                    #     requestId=id_Request
                    # ))

                    print(response.message)


            #------------------------------------------------------------FUNZIONE_2
            elif scelta == '2':
                print("\n\n|-------- AGGIORNAMENTO TICKER --------|\n")
                while True:
                    email = input("Inserisci l'email relativa all'utente di cui si vuole aggiornare il ticker: ")
                    email_valid = verifyEmail(email)
                    if email_valid:
                        break
                    print("Formato email errato!")
                while True:
                    ticker = input("Inserisci il nuovo ticker: ")
                    ticker_valid = verifyTicker(ticker)
                    if ticker_valid:
                        break            
                    
                if email_valid and ticker_valid:
                    operation = 'UpdateTicker'
                    id_Request = generateIdRequest(operation, email, ticker)

                    response = stubCommand.UpdateTicker(op_pb2.UpdateTickerRequest(
                        email=email, 
                        ticker=ticker,
                        requestId=id_Request,
                    ))
                    print(response.message)

            #------------------------------------------------------------FUNZIONE_3 
            elif scelta == '3':
                print("\n\n|-------- AGGIORNAMENTO SOGLIE --------|\n")
                while True:
                    email = input("Inserisci l'email relativa all'utente di cui si vogliono modificare i valori: ")
                    email_valid = verifyEmail(email)
                    if email_valid:
                        break
                    print("Formato email errato!")

                while True:
                    while True:
                        sceltaHigh = input("Vuoi modificare il valore di soglia massima?(y/n) ")
                        if sceltaHigh == "y" or sceltaHigh == "n":
                            if sceltaHigh == "y":
                                highValue = float(input("Inserisci il nuovo high value: "))
                            else:
                                highValue = None
                                print("High value non modificato")
                            break
                        print("Scelta non valida")
                    
                    while True:
                        sceltaLow = input("Vuoi modificare il valore di soglia minima?(y/n) ")
                        if sceltaLow == "y" or sceltaLow == "n":
                            if sceltaLow == "y":
                                lowValue = float(input("Inserisci il nuovo low value: "))
                            else:
                                lowValue = None
                                print("Low value non modificato")
                            break
                        print("Scelta non valida")

                    if checkValue(highValue,lowValue):
                        break
                    else:
                        print("Errore: la soglia minima è maggiore della soglia massima. Reinserisci i dati")
                    
                if email_valid:
                    operation = 'UpdateValues'
                    id_Request = generateIdRequest(operation, email)
                    response = stubCommand.UpdateValues(op_pb2.UpdateValuesRequest(
                        email=email, 
                        requestId=id_Request,
                        highValue=highValue,
                        lowValue=lowValue
                    ))
                    print(response.message)

            #------------------------------------------------------------FUNZIONE_4
            elif scelta == '4':
                print("\n\n|-------- ELIMINAZIONE UTENTE --------|\n")
                while True:
                    email = input("Inserisci l'email relavita all'utente che si vuole eliminare: ")
                    if verifyEmail(email):
                        break
                    print("Formato email errato!")

                operation = 'DeleteUser'
                id_Request = generateIdRequest(operation, email)

                response = stubCommand.DeleteUser(op_pb2.DeleteUserRequest(
                    email=email,
                    requestId = id_Request
                ))
                print(response.message)

            #------------------------------------------------------------FUNZIONE_5
            elif scelta == '5':
                print("\n\n|-------- ULTIMO VALORE DISPONIBILE/TICKER --------|\n")
                while True:
                    while True:
                        email = input("Inserisci l'email relavita all'utente da cui recuperare il valore: ")
                        if verifyEmail(email):
                            break
                        print("Formato email errato!")

                    response = stubQuery.GetLatestValue(op_pb2.GetLatestValueRequest(email=email))
                    if not response.email:
                        print("Errore: Utente non esistente.")
                    elif not response.value and not response.timestamp:
                        print("Errore: Nessun dato finanziario trovato per il ticker.")
                    else:
                        print(f"Ultimo valore di {response.ticker}: {response.value} | (Timestamp: {response.timestamp})")
                        break

            #------------------------------------------------------------FUNZIONE_6
            elif scelta == '6':
                print("\n\n|-------- MEDIA VALORI TICKER --------|\n")
                while True:
                    while True:
                        email = input("Inserisci l'email relavita all'utente: ")
                        email_valid = verifyEmail(email)
                        if email_valid:
                            break
                        print("Formato email errato!")
                    while True:
                        try: 
                            numValue = int(input("Inserisci il numero di valori per eseguire la media: "))
                            if numValue > 0:
                                break
                            else:
                                print("Non puoi inserire un valore negativo o zero!")
                        except ValueError:
                            print("Errore: devi inserire un numero intero valido!")

                    if email_valid and numValue > 0:
                        response = stubQuery.CalcAvarageValue(op_pb2.CalcAvarageValueRequest(email=email, count=numValue))
                        if not response.email:
                            print("Errore: Utente non esistente.")
                        elif not response.averageValue:
                            print("Errore: Nessun dato disponibile per calcolare la media.")
                        else:
                            print(f"Il valore medio di {response.ticker} è {response.averageValue}")
                            break
                    
            #------------------------------------------------------------ALTRO
            elif scelta == '7':
                print("\nEsco!")
                break

            else:
                print("\nScelta non valida, riprova.")


if __name__ == "__main__" : 
    logging.basicConfig()
    run()