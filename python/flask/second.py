from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def logincheck():
    username = request.form['username']
    password = request.form['password']
    if username == 'admin' and password == 'password':
        return render_template('login.html', message='success', login=True, username=username)
    return render_template('login.html', message='username or password wrong', username=username)

if __name__ == '__main__':
    app.run()
