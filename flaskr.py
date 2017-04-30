import os
import sqlite3
from forms import SignupForm
import re
from behave import *
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash


app = Flask(__name__)
# os.chdir('E:\\Flaskr\\flaskr')
# conn = sqlite3.connect(r'./flaskr/flaskr.db')
# db = conn.cursor()
# sql = '''select * from users'''
# results = db.execute(sql)
# all_users = results.fetchall()
app.config.from_object(__name__)
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'flaskr_test.db'),
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

os.environ['FLASK_APP'] = 'flaskr' # to avoid error msg


def connect_db():
    """ Connect to database """
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv


def get_db():
    if not hasattr(g, "sqlite_db"):
        g.sqlite_db = connect_db()
    return g.sqlite_db


@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()
    # if app.environment == 'test':
    #    os.unlink(app.config['DATABASE']) # can't delete here


def init_db(schema='schema.sql'):
    db = get_db()
    with app.open_resource(schema, mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()

@app.route('/')
def show_entries():
    db=get_db()
    cur = db.execute("select * from users order by username desc")
    rows = cur.fetchall()
    for i in rows:
        print(i)
    return render_template('home_page.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm(request.form)

    if request.method == 'POST':
        _name = request.form['name']
        _email = request.form['email']
        _password = request.form['password']
        _confirm_password=request.form['confirm_password']

        if _password != _confirm_password:
            flash(u'Password and confirm password are not the same', None)
            return render_template('sign_up.html', form = form, error = flash)

        x = True
        while x:
            if (len(_password) < 8 ):
                break
            elif not re.search("[a-z]", _password):
                break
            elif not re.search("[0-9]", _password):
                break
            elif not re.search("[A-Z]", _password):
                break
            elif re.search("\s", _password):
                break
            else:
                # flash("Valid Password")
                x = False

        if x:
            flash("Not a Valid Password")
            return render_template('sign_up.html', form=form)

        # validate the received values
        if _name and _email and _password:
            con = sqlite3.connect(app.config['DATABASE'])
            cur = con.cursor()
            cur.execute("INSERT INTO users (username,email,password) VALUES (?,?,?)",
                        (_name, _email, _password))
            con.commit()
            con.close()
            flash("Register successful")
            return render_template('show_entries.html')
        else:
            return 'Enter the required fields'

    elif request.method == 'GET':
        return render_template('sign_up.html', form = form)


@app.route('/login', methods=['GET', 'POST'])
def login():
        error = None
        if request.method == 'POST':
            username = request.form['username']
            email = request.form['email']
            password = request.form['password']
            if username and password:
                db = get_db()
                cur = db.execute("select *  from users where username =? and email=? and password=?", [username, email, password])
                rows = cur.fetchone()
                if rows:
                    session['logged_in'] = True
                    flash("Login Success!")
                else:
                    error = "Bad Login"
            else:
                error = "Missing user credentials"
        return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_entries'))

def serve_forever():
    app.run()


def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError("Not running with Werkzeug server")
    if app.environment == 'test':
        func()
        os.unlink(app.config['DATABASE'])


@app.route('/shutdown')
def shutdown():
    if app.environment == 'test':
        shutdown_server()
    return "Server shutdown"

@app.cli.command('start')
def start():
    app.config.from_object(__name__) # load config from this file

    app.config.update(dict(
        DATABASE=os.path.join(app.root_path, 'flaskr_test.db'),
        SECRET_KEY='Production key',
    ))
    app.config.from_envvar('FLASKR_SETTINGS',  silent=True)

    app.run()


def test_server():
    ### Setup for integration testing
    app.config.from_object(__name__) # load config from this file

    app.config.update(dict(
        DATABASE=os.path.join(app.root_path, 'flaskr_test.db'),
        SECRET_KEY='Test key',
        SERVER_NAME='localhost:5000',
        Login_NAME='localhost/login:5000',
        # DEBUG=True, # does not work from behave
    ))
    app.environment = 'test'
    with app.app_context():
        init_db('test_schema.sql')
    app.run()

if __name__ == '__main__':

        app.run()




