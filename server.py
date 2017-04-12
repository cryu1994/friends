from flask import Flask, render_template, redirect, request, session, flash
from mysqlconnection import MySQLConnector

app = Flask(__name__)
mysql = MySQLConnector(app, 'friendsdb')
app.secret_key = 'fdsfdsa234'
@app.route('/')
def show():
    query = "SELECT * FROM friends"
    friends = mysql.query_db(query)
    return render_template('index.html', all_friends=friends)


@app.route('/create', methods=['post'])
def create():
    print request.form['name']
    print request.form['age']
    query = "INSERT INTO friends(name, age, created_at, updated_at) VALUES(:name, :age, NOW(), NOW())"

    data = {
        'name': request.form['name'],
        'age': request.form['age'],
    }
    mysql.query_db(query, data)
    return redirect('/', )
app.run(debug=True)
