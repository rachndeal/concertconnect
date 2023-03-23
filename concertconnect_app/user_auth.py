import sqlite3
from flask import Flask, session, redirect, url_for, render_template, request

app = Flask(__name__)
app.secret_key = 'some_secret_key'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE email = ? AND password = ?", (email, password))
        user = cursor.fetchone()
        if user:
            session['email'] = user[1]
            session['role'] = user[4]
            return redirect(url_for('index'))
        else:
            return render_template('login.html', error='Invalid email or password')
    else:
        return render_template('login.html')

@app.route('/')
def index():
    if 'email' in session:
        if session['role'] == 'venue owner':
            # show venue owner functionalities
            return render_template('venue_owner.html')
        else:
            # show normal user functionalities
            return render_template('normal_user.html')
    else:
        return redirect(url_for('login'))
def authenticate_user(username, password):
    # check if the user exists in the database and their password matches
    user = get_user_from_database(username)
    if (user and user.get('password') == password):
        # return the user's role
        return user.get('role')
    else:
        # return None if authentication fails
        return None
