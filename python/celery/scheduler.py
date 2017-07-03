from celery import Celery
from selenium import webdriver
import threading

app = Celery('tasks', backend='amqp://guest:guest@localhost:5672//',
             broker='amqp://guest:guest@localhost:5672//')

options = webdriver.ChromeOptions()
options.binary_location = "/usr/sbin/chromium"
options.add_argument("headless")
options.add_argument("window-size=1200x600")
driver = webdriver.Chrome(chrome_options=options)


def work(url):
    driver.get(url)
    title = driver.title
    print(title)


@app.task
def get(url, n=0):
    thread = []

    for i in range(10):
        print("Now to get " + str(i))
        t = threading.Thread(target=work, args=(url,))
        thread.append(t)

    for i in range(0, 10):
        thread[i].start()

    for i in range(0, 10):
        thread[i].join()
