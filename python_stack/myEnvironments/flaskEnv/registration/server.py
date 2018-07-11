from flask import Flask, render_template, request, redirect, session, flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
app = Flask(__name__)
app.secret_key = 'magic'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    check = True
    if len(request.form['first_name']) < 1:
        flash('Error! Invalid first name!', 'wrong')
        check = False
    elif not request.form['first_name'].isalpha():
        flash('First name has non-alpha character!', 'wrong')
        check = False
    if len(request.form['last_name']) < 1:
        flash('Error! Invalid last name!', 'wrong')
        check = False
    elif not request.form['last_name'].isalpha():
        flash('Last name has a non-alpha character!', 'wrong')
        check = False
    if len(request.form['email']) < 1:
        flash('Error! Invalid email', 'wrong')
        check = False
    elif not EMAIL_REGEX.match(request.form['email']):
        flash('Invalid email format!', 'wrong')
        check = False
    if len(request.form['password']) < 6:
        flash('Password must contain at least 6 characters!', 'wrong')
        check = False
    if request.form['password'] != request.form['confirm_password']:
        flash('Password does not match!', 'wrong')
        check = False

    if check == True:
        flash('Success!', 'success')
    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    return redirect('/')

app.run(debug=True)