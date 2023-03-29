from flask import Flask, render_template, request, redirect, url_for, flash
import matplotlib.pyplot as plt
import data_processor as dp


app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('status'))

@app.route('/status')
def status():
    return render_template('status.html')

@app.route('/poc')
def poc():
    data = "Hello World!"
    return render_template('poc.html', data=data)

def run():
    app.run(host='localhost', port=5000, debug=True)

if __name__ == '__main__':
    run()