import pika

# Conexão com o servidor RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declarar a exchange do tipo 'fanout'
channel.exchange_declare(exchange='minha_fanout_exchange', exchange_type='fanout')

# Criar as duas filas (queues)
channel.queue_declare(queue='fila_1')
channel.queue_declare(queue='fila_2')

# Vincular as filas à exchange 'fanout'
channel.queue_bind(exchange='minha_fanout_exchange', queue='fila_1')
channel.queue_bind(exchange='minha_fanout_exchange', queue='fila_2')

# Enviar uma mensagem para a exchange
message = "Mensagem para as filas"
channel.basic_publish(exchange='minha_fanout_exchange', routing_key='', body=message)
print(f"Mensagem enviada: {message}")

# Fechar a conexão
connection.close()

