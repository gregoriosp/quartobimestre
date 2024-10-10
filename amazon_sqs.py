import boto3

# Configurar o cliente SQS
sqs = boto3.client('sqs', region_name='us-east-1')  # Especifique sua região

# Definir a URL da fila SQS
queue_url = 'https://sqs.us-east-1.amazonaws.com/123456789012/minha-fila'

# Enviar uma mensagem para a fila
response = sqs.send_message(
    QueueUrl=queue_url,
    MessageBody='Este é o conteúdo da mensagem'
)

# Imprimir o ID da mensagem enviada
print(f"Mensagem enviada com ID: {response['MessageId']}")
