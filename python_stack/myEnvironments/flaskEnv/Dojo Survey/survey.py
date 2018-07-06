from flask import Flask, render_template, request, redirect
app=Flask(__name__)

@app.route('/')
def survey():
    return render_template('index.html') 

@app.route('/result', methods=["POST"])
def results():
    result= request.form["name"]+ request.form["location"]+ request.form["language"]+ request.form["comment"]
    return result
app.run(debug=True)
