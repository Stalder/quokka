import pika
import sys
import json
from PIL import Image
import random

credentials = pika.PlainCredentials('Raccoon', 'CoolRaccoon')
parameters = pika.ConnectionParameters('192.168.43.215', credentials=credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()
index = 0

channel.queue_declare(queue='task_queue', durable=True)

paths = ['1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg', '6.jpg']
for path in paths:
    image = Image.open('C:\\Users\Zver\Desktop\Photo/' + path)
    size = image.size
    pix = list(image.getdata())
    obj = json.dumps({'weight': size[0], 'height': size[1], 'image': pix, 'queue_name': 'queue_name'})
    message = ' '.join(sys.argv[1:]) or obj
    channel.basic_publish(exchange='',
                          routing_key='task_queue',
                          body=message,
                          properties=pika.BasicProperties(
                              delivery_mode=2,  # make message persistent
                          ))
    print(" [x] Sent  ")


def callback(ch, method, properties, body):
    global index
    parsed = json.loads(body.decode())
    pixlist = list(parsed['image'])
    new_image = Image.new('L', (parsed['weight'], parsed['height']))
    new_image.putdata(pixlist)
    new_image.save(str(index) + '.jpg')
    index += 1
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=1)
channel.basic_consume(callback,
                      queue='img_queue')

channel.start_consuming()

connection.close()