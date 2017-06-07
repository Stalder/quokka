import pika
import sys

credential = pika.PlainCredentials('Raccoon', 'CoolRaccoon')
paramms = pika.ConnectionParameters('192.168.0.101', credentials=credential)
connection = pika.BlockingConnection(paramms)
channel = connection.channel()

channel.queue_declare(queue='hello')

message = ' '.join(sys.argv[1:]) or "Hello World!..."
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body=message.encode())
print(" [x] Sent %r" % (message.encode(),))

connection.close()
