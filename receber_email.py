import pika
import smtplib
import json
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Função para enviar o e-mail
def send_email(to_email, subject, body):
    # Configurações do servidor SMTP do Gmail
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    sender_email = "greggorio.895@gmail.com"  # Substitua pelo seu e-mail
    sender_password = "Bgmf+8521"  # Substitua pela sua senha

    # Criar o e-mail
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Conectar ao servidor SMTP
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Habilitar a criptografia TLS
        server.login(sender_email, sender_password)
        
        # Enviar o e-mail
        server.sendmail(sender_email, to_email, msg.as_string())
        print(f"E-mail enviado para {to_email}")
        
        # Fechar a conexão
        server.quit()
    except Exception as e:
        print(f"Erro ao enviar o e-mail: {e}")

# Conectar ao RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declarar a fila (caso ainda não exista)
channel.queue_declare(queue='email_queue')

# Função de callback para processar mensagens da fila
def callback(ch, method, properties, body):
    email_data = json.loads(body)
    to_email = email_data['to_email']
    subject = email_data['subject']
    body = email_data['body']
    
    # Enviar o e-mail
    send_email(to_email, subject, body)

# Consumir mensagens da fila
channel.basic_consume(queue='email_queue', on_message_callback=callback, auto_ack=True)

print('Aguardando mensagens...')

# Manter o consumidor em execução
channel.start_consuming()
