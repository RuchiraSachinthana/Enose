from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors

app = Flask(__name__)

#app.secret_key = 'your_secret_key'  # Change this to a strong secret key

app.config['MYSQL_HOST'] = 'your_mysql_host'
app.config['MYSQL_USER'] = 'your_mysql_user'
app.config['MYSQL_PASSWORD'] = 'your_mysql_password'
app.config['MYSQL_DB'] = 'your_mysql_db'

mysql = MySQL(app)

@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
    message = ''
    if request.method == 'POST' and 'uname' in request.form and 'psw' in request.form:
        uname = request.form['uname']
        psw = request.form['psw']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM user_login WHERE uname = %s AND psw = %s', (uname, psw,))
        user = cursor.fetchone()
        if user:
            session['loggedin'] = True
            session['uname'] = user['uname']
            session['psw'] = user['psw']
            message = 'Logged in successfully!'
            return render_template('details.html', message=message)
        else:
            message = 'Please enter correct username/password!'
    return render_template('login.html', message=message)

@app.route('/insert_data', methods=['POST'])
def insert_data():
    if 'loggedin' in session:
        if request.method == 'POST':
            label = request.form['label']
            length = request.form['length']
            circum = request.form['circum']
            csv = request.form['csv']
            time = request.form['time']

            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute(
                'INSERT INTO your_table_name (label, length, circum, csv, time) VALUES (%s, %s, %s, %s, %s)',
                (label, length, circum, csv, time)
            )
            mysql.connection.commit()
            cursor.close()

            message = 'Data inserted successfully!'
            return render_template('details.html', message=message)
    else:
        return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(debug=True)

