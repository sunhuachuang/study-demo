from celery import Celery
import datetime

app = Celery('hello', broker='amqp://guest@localhost//',
             backend="amqp://guest@localhost//")


@app.task
def hello(a):
    print(datetime.datetime.now())
