import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare('hello')

print(' [*] Waiting for messages. To exit press CTRL+C ')


def callback(channel, method, properties, body):
    print(" [x] Received %r" % (body,))


channel.basic_consume(callback, queue='hello', no_ack=True)

channel.start_consuming()
