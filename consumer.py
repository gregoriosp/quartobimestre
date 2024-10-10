import pika

# Conectar ao servidor RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declarar a fila (certifique-se de que ela exista)
channel.queue_declare(queue='aula23')

# Função callback que será chamada quando uma nova mensagem chegar
def callback(ch, method, properties, body):
    print(f"Mensagem recebida: {body.decode()}")

# Dizer ao RabbitMQ para enviar mensagens para a função callback
channel.basic_consume(queue='aula23', on_message_callback=callback, auto_ack=True)

print('Aguardando mensagens. Pressione CTRL+C para sair.')
# Manter o script em execução para receber mensagens
channel.start_consuming()

