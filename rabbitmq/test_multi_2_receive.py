import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)


channel = connection.channel()
channel.queue_declare(queue='hello2')
channel.basic_consume(callback, queue='hello2', no_ack=True)

print(' [*] Waiting for hello2. To exit press CTRL+C')
channel.start_consuming()
