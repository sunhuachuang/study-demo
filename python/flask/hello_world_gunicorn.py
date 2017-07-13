from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return 'hello word'

# gunicorn -k gevent -w 4 -b 127.0.0.1:4000 hello_world_gunicorn:app 9000多
