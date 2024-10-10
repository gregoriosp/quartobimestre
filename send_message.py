import pika

def main():
    # Parâmetros de conexão
    rabbitmq_host = 'localhost'  # Endereço do servidor RabbitMQ
    queue_name = 'aula23'         # Nome da fila para enviar a mensagem

    # Estabelecendo a conexão com o RabbitMQ
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbitmq_host))
    channel = connection.channel()

    # Declarando uma fila (a fila será criada se não existir)
    channel.queue_declare(queue='aula23')

    # Mensagem a ser enviada
    message = 'Aprendendo sobre serviços de mensageria para o curso de versionamento!'

    # Enviando a mensagem para a fila
    channel.basic_publish(exchange='',
                          routing_key=queue_name,
                          body=message)

    print(f" [x] Sent '{message}'")

    # Fechando a conexão
    connection.close()

if __name__ == '__main__':
    main()



