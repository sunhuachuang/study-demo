import os, sqlite3, hashlib
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash

app = Flask(__name__)

app.config.from_object(__name__)
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'blog.db'),
    SECRET_KEY='developmentkey',
    ADMIN='sun',
    PASSWORD='sun'
))
app.config.from_envvar('BLOG_SETTINGS', silent=True)

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


@app.route('/')
def index():
    cur = get_db().execute('select id, title, content from articles order by id desc')
    articles = cur.fetchall()
    return render_template('index.html', articles=articles)

@app.route('/show/<article_id>', methods=['GET', 'POST'])
def show(article_id):
    if request.method == 'POST' and request.form['content']:
        if not session.get('logged_in'):
            return redirect(url_for('login'))
        db = get_db()
        db.execute('insert into comments (content, article_id, user_id) values (?, ?, ?)', [request.form['content'], int(article_id), session.get('user')['id']])
        db.commit()
        flash('New comment was successful add!')
        redirect(url_for('show', article_id=article_id))
    db = get_db()
    article = db.execute('select id, title, content from articles where id=?', article_id).fetchone()
    comments = db.execute('select id, content from comments where article_id=?', article_id).fetchall()
    return render_template('show.html', article=article, comments=comments)

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if not session.get('admin'):
        return redirect(url_for('login'))

    if request.method == 'POST' and request.form['title'] and request.form['content']:
        db = get_db()
        db.execute('insert into articles (title, content) values (?, ?)', [request.form['title'], request.form['content']])
        db.commit()
        flash('success create a title!')
        redirect(url_for('admin'))

    cur = get_db().execute('select id, title, content from articles order by id desc')
    articles = cur.fetchall()
    return render_template('admin.html', articles=articles)

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST' and request.form['username'] and request.form['password']:
        if request.form['username'] == app.config['ADMIN'] and request.form['password'] == app.config['PASSWORD']:
            session['logged_in'] = True
            session['admin'] = True
            session['user'] = {'id': 1000, 'username': 'admin'}
            flash('You were logged in')
            return redirect(url_for('index'))

        username = request.form['username']
        user = get_db().execute('select id, username, password from users where username=?', (username,)).fetchone()
        user = dict(user)
        m = hashlib.md5()
        m.update(request.form['password'].encode('utf-8'))
        if m.digest() != user['password']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            session['admin'] = False
            session['user'] = user
            flash('You were logged in')
            return redirect(url_for('index'))
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out!')
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    error = None
    print(request.method)
    if request.method == 'POST':
        if not request.form['username'] or not request.form['password']:
            flash('not value!')
        else:
            db = get_db()
            m = hashlib.md5()
            m.update(request.form['password'].encode('utf-8'))
            db.execute('insert into users (username, password) values (?, ?)', [request.form['username'], m.digest()])
            db.commit()
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('index'))
    return render_template('register.html')

if __name__ == '__main__':
    app.run()
