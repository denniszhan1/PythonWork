from flask import Flask, render_template, redirect, request
from mysqlconnection import MySQLConnector

app = Flask(__name__)
mysql = MySQLConnector(app, 'full_friends')

@app.route('/')
def index():
    query = "SELECT * FROM friends"
    full_friends = mysql.query_db(query)
    return render_template("index.html", friends = full_friends)

@app.route('/add', methods = ['POST'])
def add():
    query = "INSERT INTO friends (first_name, last_name, occupation, created_at, updated_at) VALUES (:first_name, :last_name, :occupation, NOW(), NOW())"
    data = { 'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'occupation': request.form['occupation']
    }
    mysql.query_db(query, data)
    return redirect('/')

app.run(debug=True)