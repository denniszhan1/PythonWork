from flask import Flask, render_template, request, redirect
app=Flask(__name__)

@app.route('/')
def noninjas():
    return "No ninjas here"

@app.route('/ninja')
def ninjas():
    color='none'
    return render_template ("index.html", color=color)

@app.route('/ninja/<color>')
def getcolor(color):
    return render_template('index.html', color=color)



app.run(debug=True)
