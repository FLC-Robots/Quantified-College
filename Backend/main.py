import flask
import threading


app = flask.Flask(__name__)

@app.route('/')
def index():
    return flask.render_template('index.html')


def run():
    app.run(host='localhost', port=5000, debug=True)

if __name__ == '__main__':
    run()