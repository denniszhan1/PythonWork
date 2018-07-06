from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key='ThisIsSecret'

@app.route('/')
def index():
    if 'count' in session:
      session['count'] +=1
    else:
      session['count']=1
    return render_template('index.html', count=session['count'])

@app.route('/two', methods=['POST'])
def plustwo():
    if 'count' in session:
      session['count'] +=1
    else:
      session['count']=2
    return redirect('/')

@app.route('/users', methods=['POST'])
def create_user():
    print "Got Post Info"
  
    session['name'] = request.form['name']
    session['email'] = request.form['email']
    
    return redirect ('/show')

@app.route('/show')
def show_user():
    return render_template('user.html', name=session['name'], email=session['email'])

@app.route('/reset')
def clear():
    session['count']=0
    return redirect('/')

app.run(debug=True)