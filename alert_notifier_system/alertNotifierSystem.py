from confluent_kafka import Consumer, KafkaError
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import json

def send_email(to_email, subject, body, smtp_server, smtp_port, email_address, email_password):
    msg = MIMEMultipart()
    msg['From'] = email_address
    msg['To'] = to_email
    msg['Subject'] = subject
    
    msg.attach(MIMEText(body, 'plain'))
    
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(email_address, email_password)
        text = msg.as_string()
        server.sendmail(email_address, to_email, text)
        server.quit()
        print(f"Email inviata con successo a {to_email}!")
    except Exception as e:
        print(f"Errore nell'invio dell'email a {to_email}: {e}")


def alertNotifier():
    smtp_config = {
        'server': 'smtp.gmail.com',
        'port': 587,
        'address': 'giorgiodb2000@gmail.com',
        'password': 'wxzj olzk kjcx didx'
    }

    consumer_config = {
        'bootstrap.servers': 'kafka:9092',
        'group.id': 'group2',
        'auto.offset.reset': 'earliest',
        'enable.auto.commit': True,
        'auto.commit.interval.ms': 5000
    }

    topic_to_notify = 'to-notifier'

    consumer = Consumer(consumer_config)
    consumer.subscribe([topic_to_notify])

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
            
            alert_message = json.loads(msg.value().decode('utf-8'))
            email = alert_message.get('email')
            ticker = alert_message.get('ticker')
            condition = alert_message.get('condition')
            price = alert_message.get('price')
            threshold = alert_message.get('threshold')

            if not email or not ticker or not condition:
                print("Messaggio alert incompleto.")
                continue

            subject = f"Notifica Alert per {ticker}"
            if condition == 'high':
                body = f"Il prezzo di {ticker} ha superato la soglia massima di {threshold}. Prezzo attuale: {price}."
            elif condition == 'low':
                body = f"Il prezzo di {ticker} è sceso al di sotto della soglia minima di {threshold}. Prezzo attuale: {price}."
            else:
                body = "Condizione di alert non riconosciuta."

            send_email(
                to_email=email,
                subject=subject,
                body=body,
                smtp_server=smtp_config['server'],
                smtp_port=smtp_config['port'],
                email_address=smtp_config['address'],
                email_password=smtp_config['password']
            )
    except KeyboardInterrupt:
        print("Consumer interrotto dall'utente.")
    finally:
        consumer.close()

def main():
    print("AlertNotifierSystem in ascolto sul topic 'to-notifier'...")
    alertNotifier()

if __name__ == "__main__":
    main()