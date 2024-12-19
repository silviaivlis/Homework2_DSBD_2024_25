from database import Session, FinancialData, Users
from confluent_kafka import Consumer, Producer, KafkaError
import json
import time

def deliveryReport(err, msg):
    if err:
        print(f"Consegna messaggio fallita: {err}")
    else:
        print(f"Messaggio consegnato al topic {msg.topic()} con partizione [{msg.partition()}] e offset {msg.offset()}")


def alertSystem():
    consumer_config = {
        'bootstrap.servers': 'kafka:9092',
        'group.id': 'group1',
        'auto.offset.reset': 'earliest',
        'enable.auto.commit': True,
        'auto.commit.interval.ms': 5000
    }

    max_retries = 20
    delay = 20

    topic_to_alert = 'to-alert-system'
    topic_to_notify = 'to-notifier'

    for _ in range(1, max_retries+1):
        try:
            producer = Producer({'bootstrap.servers': 'kafka:9092'})
            producer.produce(topic_to_notify, 'test-connection')
            producer.flush(10)
            print("Connessione a Kafka riuscita.")
            break
        except Exception as e:
            print(f"Connessione fallita: {e}. Riprovo tra {delay} secondi...")
            time.sleep(delay)
    else:
        raise RuntimeError("Impossibile connettersi a Kafka dopo vari tentativi.")


    consumer = Consumer(consumer_config)
    consumer.subscribe([topic_to_alert])


    try:
        while True:
            msg = consumer.poll(1.0)
            if msg is None:
                continue
            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    print(f"End of partition reached {msg.topic()} [{msg.partition()}]")
                else:
                    print(f"Consumer error: {msg.error()}")
                continue
            
            data = json.loads(msg.value().decode('utf-8'))

            if data.get('data') == 'Ciclo di raccolta dati completato':
                print("Ricevuto messaggio di raccolta dati.")

                with Session() as session:
                    users = session.query(Users).all()
                    for user in users:
                        ticker_data = session.query(FinancialData).filter_by(ticker=user.ticker).order_by(FinancialData.timestamp.desc()).first()
                        if not ticker_data:
                            continue
                        
                        price = ticker_data.value

                        alert_condition = None

                        if user.highValue is not None and price > user.highValue:
                            alert_condition = 'high'
                        elif user.lowValue is not None and price < user.lowValue:
                            alert_condition = 'low'
                        
                        if alert_condition is not None:
                            alert_message = {
                                'email': user.email,
                                'ticker': user.ticker,
                                'condition': alert_condition,
                                'price': price,
                                'threshold': user.highValue if alert_condition == 'high' else user.lowValue
                            }
                            
                            producer.produce(topic_to_notify, json.dumps(alert_message), callback=deliveryReport)
                            producer.flush()
                            print(f"Alert per {user.email} su {user.ticker}: {alert_condition} value.")

    except KeyboardInterrupt:
        print("Consumer interrotto dall'utente.")
    finally:
        consumer.close()

def main():
    print("AlertSystem in ascolto sul topic 'to-alert-system'...")
    alertSystem()

if __name__ == "__main__":
    main()