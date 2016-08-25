from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return '<h1>Home</h1>'

@app.route('/login', methods=['GET'])
def login():
    return '''<form action="/login" method="post">
              <p><input name="username"></p>
              <p><input name="password" type="password"></p>
              <p><button type="submit">Sign In</button></p>
              </form>'''

@app.route('/login', methods=['POST'])
def logincheck():
    if request.form['username'] == 'admin' and request.form['password'] == 'password':
        return '<h2>Hello, admin!</h2>'
    return '<h2>username or password wrong</h2>'

if __name__ == '__main__':
    app.run()
