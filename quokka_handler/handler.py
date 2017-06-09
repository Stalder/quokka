import pika
import json
from PIL import Image

credentials = pika.PlainCredentials('Raccoon', 'CoolRaccoon')
parameters = pika.ConnectionParameters('192.168.43.215', credentials=credentials)
connection = pika.BlockingConnection(parameters)

channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)
print(' [*] Waiting for messages. To exit press CTRL+C')


def handle_img(img):
    img = img.resize((1000, 1000), Image.ANTIALIAS)
    width, height = img.size
    pix1 = img.load()
    new = Image.new('L', (1000, 1000))
    pix2 = new.load()
    for i in range(width):
        for j in range(height):
            pix2[i, j] = \
                (pix1[i, j][0] +
                 pix1[i, j][1] +
                 pix1[i, j][2]) // 3
    return new


def sent_back(img, queue_name, img_name):
    channel.queue_declare(queue=queue_name, durable=True)
    image = handle_img(img)
    image.save('1.jpg')
    size = image.size
    pix = list(image.getdata())
    msg = json.dumps({'weight': size[0], 'height': size[1], 'image': pix, 'queue_name': queue_name})
    channel.basic_publish(exchange='',
                          routing_key=queue_name,
                          body=msg,
                          properties=pika.BasicProperties(
                              delivery_mode=2,  # make message persistent
                          ))
    print('hi')
    print(" [x] Sent  ")


def callback(ch, method, properties, body):
    # print(" [x] Received %r" % (body,))
    parsed = json.loads(body.decode())
    pixlist = [tuple(x) for x in list(parsed['image'])]
    new_image = Image.new('RGB', (parsed['weight'], parsed['height']))
    new_image.putdata(pixlist)
    new_image.save('est.jpg')
    sent_back(new_image, 'img_queue', '1')

    ch.basic_ack(delivery_tag=method.delivery_tag)
    print(' [x] Done ')


channel.basic_qos(prefetch_count=1)
channel.basic_consume(callback,
                      queue='task_queue')

channel.start_consuming()