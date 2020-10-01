from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('home.html')

@app.route('/new')
def rajat():
    return render_template('new.html')

app.run(debug = True)