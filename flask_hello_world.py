from flask import Flask, request, redirect, url_for, abort
import random
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello world!'


@app.route('/suca/<name>', methods=['GET'])
def suca_forte(name):
    if request.method == 'GET':
        return 'Secondo i miei calcoli %s ha sucato il cazzo %s volte' % (name, random.randint(1, 100))
    else:
        return 'Whhops wrong request'


@app.route('/noway')
def noway():
    abort(404)


@app.route('/loginerror')
def red():
    return redirect(url_for('noway'))


if __name__ == '__main__':
    app.run()
