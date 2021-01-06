from flask import Flask, render_template

app = Flask(__name__)


@app.route('/favicon.ico')
def favicon():
    return app.send_static_file("favicon.ico")


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/about')
def about():
    return '<h1>About:</h1>'


@app.route('/hello/<whom>')
def hello(whom):
    # return f'<h1>Hello {whom}</h1>'
    return render_template('hello.html', whom=whom)


@app.route('/100_plus/<int:n>')
def adder(n):
    return f'100+{n}={100+n}'
