from celery import Celery

app = Celery('hello', broker='amqp://guest@localhost//',
             backend="amqp://guest@localhost//")


@app.task
def hello():
    for i in range(10):
        yield i
