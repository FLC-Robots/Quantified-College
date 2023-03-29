from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import data_processor as data_p

import base64
from io import BytesIO
from matplotlib.figure import Figure

dp = data_p.data_processor()
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

@app.route('/test')
def test():
    fig = Figure()
    ax = fig.subplots()
    ax.plot([1, 2])
    # Save it to a temporary buffer.
    buf = BytesIO()
    fig.savefig(buf, format="png")
    # Embed the result in the html output.
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return render_template('test.html', data=data)

def run():
    app.run(host='localhost', port=5000, debug=True)

if __name__ == '__main__':
    run()