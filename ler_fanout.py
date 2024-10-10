import pika

def callback(ch, method, properties, body):
    print(f"Mensagem recebida da fila_1: {body.decode()}")
    print(f"Mensagem recebida da fila_2: {body.decode()}")

# Conectar ao RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Garantir que a fila_1 existe
channel.queue_declare(queue='fila_1')
channel.queue_declare(queue='fila_2')

# Consumir as mensagens da fila_1
channel.basic_consume(queue='fila_1', on_message_callback=callback, auto_ack=True)
channel.basic_consume(queue='fila_2', on_message_callback=callback, auto_ack=True)

print('Aguardando mensagens da fila_1. Pressione CTRL+C para sair.')
channel.start_consuming()

