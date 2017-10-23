import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    time.sleep(3)

    channel.basic_publish(exchange='', routing_key='hello2', body=body)


channel.queue_declare(queue='hello1')
channel.basic_consume(callback, queue='hello1', no_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
