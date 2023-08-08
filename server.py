from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = '20c64a72d3d7dffc39ba1e8ae9421b857805fef856f551650b8b802e97b3d3aa'

@app.route('/')
def index():

    if 'num' not in session:
        session['num'] = 0
    session['num'] += 1
    return render_template('index.html')

@app.route('/addtwonum')
def count():
    session['num'] += 1
    return redirect('/')

@app.route('/adding', methods = ['POST'])
def progress():
    num = int(request.form['add']) - 1
    session['num'] += num
    return redirect ('/')

@app.route('/reset')
def clear_session():
    session.clear()
    return redirect('/')
    
if __name__ == '__main__':
    app.run(debug=True)