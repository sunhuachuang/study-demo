from celery import Celery
from selenium import webdriver

app = Celery('tasks', backend='amqp://guest:guest@localhost:5672//',
             broker='amqp://guest:guest@localhost:5672//')

options = webdriver.ChromeOptions()
options.binary_location = "/usr/sbin/chromium"
options.add_argument("headless")
options.add_argument("window-size=1200x600")
driver = webdriver.Chrome(chrome_options=options)


@app.task
def get(url):
    driver.get(url)
    title = driver.title
    return title
