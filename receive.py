import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare('hello')

print(' [*] Waiting for messages. To exit press CTRL+C ')


def callback(ch, method, properties, body):
    print(" [x] Received %r" % (body,))
    time.sleep(body.decode().count('.'))
    print(" [x] Done")


channel.basic_consume(callback, queue='hello', no_ack=True)

channel.start_consuming()
