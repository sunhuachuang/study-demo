import pika
import threading
import time

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')

a = 0


class myThread (threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        print("Starting " + self.name)

        time.sleep(10)

        print("Exiting " + self.name)


def callback(ch, method, properties, body):
    global a
    print(" [x] Received %r it will wait 10s" % body)
    a = a + 1
    thread1 = myThread(a)
    thread1.start()


channel.basic_consume(callback, queue='hello', no_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
