import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from RedisSession import RedisSessionInterface

app = Flask(__name__)
app.session_interface = RedisSessionInterface()

app.config.from_object(__name__)
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'main.db'),
    SECRET_KEY='developmentkey',
    USERNAME='sun',
    PASSWORD='sun'
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)


def connect_db():
    """Connect to sqlite database"""
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv


def init_db():
    db = get_db()
    with app.open_resource('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()


@app.cli.command('initdb')
def initdb_command():
    init_db()
    print('Initialized the database.')


def get_db():
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db


@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()


@app.route('/', methods=['GET', 'POST'])
def index():
    error = None
    if request.method == 'POST':
        if request.form['username']:
            cur = get_db().execute('select id, username, password from users where username=?',
                                   (request.form['username'],))
            user = cur.fetchone()
            if not user:
                error = 'no username'
            elif user['password'] == request.form['password']:
                session['username'] = user['username']
                session['id'] = user['id']
                session['logged_in'] = True
                return redirect(url_for('get_users'))
            else:
                error = 'password wrong'

    return render_template('login.html', error=error)


@app.route('/users')
def get_users():
    if not session.get('logged_in'):
        flash('must login!')
        return redirect(url_for('index'))
    cur = get_db().execute('select title, text from entries order by id desc')
    entries = cur.fetchall()
    return render_template('users.html', entries=entries)


@app.route('/users', methods=['POST'])
def post_users():
    if not session.get('logged_in'):
        flash('must login!')
        return redirect(url_for('index'))
    db = get_db()
    db.execute('insert into entries (title, text) values (?, ?)',
               (request.form['title'], request.form['text']))
    db.commit()
    flash('New entry was successful add!')
    return redirect(url_for('get_users'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    error = None
    if request.method == 'POST':
        if request.form['username'] and request.form['password']:
            cur = get_db().execute('select id, username, password from users where username=?',
                                   (request.form['username'],))
            user = cur.fetchone()
            if user:
                error = 'exists username'
            else:
                db = get_db()
                db.execute('insert into users (username, password) values (?, ?)',
                           (request.form['username'], request.form['password']))
                db.commit()
                cur = db.execute(
                    'select id, username, password from users where username=?', (request.form['username'],))
                user = cur.fetchone()
                session['username'] = user['username']
                session['id'] = user['id']
                session['logged_in'] = True
                flash('register success')
                return redirect(url_for('get_users'))
        else:
            error = 'invalid username or password'

    return render_template('register.html', error=error)


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out!')
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run()
