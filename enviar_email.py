import pika
import json

# Conectar ao RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declarar a fila
channel.queue_declare(queue='email_queue')

# Função para enviar mensagem para a fila
def send_email_to_queue(to_email, subject, body):
    email_data = {
        'to_email': to_email,
        'subject': subject,
        'body': body
    }
    
    # Publica a mensagem na fila
    channel.basic_publish(exchange='',
                          routing_key='email_queue',
                          body=json.dumps(email_data))
    print(f"Email enviado para a fila: {to_email}")

# Exemplo de envio
send_email_to_queue("greggorio.895@gmail.com", "Assunto Teste", "Corpo do e-mail teste")

# Fechar conexão
connection.close()
