# use pika
import pika

connection = pika.BlockingConnection(pika.connection.URLParameters('amqp://test:test@192.168.1.8:5672/%2F'))
channel = connection.channel()
channel.queue_declare(queue='hello')

channel.basic_publish(exchange='', routing_key='hello', body='testestetst   ello World!')

print(" [x] Sent 'Hello World!'")

connection.close()
