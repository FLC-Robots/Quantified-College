from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
#import data_processor as data_p

import base64
from io import BytesIO

import random

#dp = data_p.data_processor()
app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('test'))

@app.route('/status')
def status():
    return render_template('status.html')

@app.route('/poc')
def poc():
    data = "Hello World!"
    return render_template('poc.html', data=data)

@app.route('/test')
def test():
    return render_template('test.html')

@app.route('/data', methods=['GET'])
def data():
    return jsonify(num=random.randint(0, 100))

def run():

    app.run(host='0.0.0.0', port=5000, debug=True)

if __name__ == '__main__':
    run()