from flask import Flask, render_template, redirect, request
from todo import ToDoList

app = Flask(__name__)

todolist = ToDoList()

@app.route('/favicon.ico')
def favicon():
    return app.send_static_file("favicon.ico")


@app.route('/')
def show_todolist():
    return render_template('showtodo.html', todolist=todolist.get_all())


@app.route('/additem', methods=['POST'])
def add_item():
    title = request.form['title']
    if not title:
        return redirect('/')
    todolist.add(title)
    return redirect('/')


@app.route('/deleteitem/<int:item_id>')
def delete_todoitem(item_id):
    todolist.delete(item_id)
    return redirect('/')


@app.route('/updatedone/<int:item_id>')
def update_todoiitemdone(item_id):
    todolist.update(item_id)
    return redirect('/')


@app.route('/deletealldoneitems')
def delete_alldoneitems():
    todolist.delete_doneitem()
    return redirect('/')

# @app.route('/')
# def hello_world():
#     return 'Hello World!'
#
#
# @app.route('/about')
# def about():
#     return '<h1>About:</h1>'
#
#
# @app.route('/hello/<whom>')
# def hello(whom):
#     # return f'<h1>Hello {whom}</h1>'
#     return render_template('hello.html', whom=whom)
#
#
# @app.route('/100_plus/<int:n>')
# def adder(n):
#     return f'100+{n}={100+n}'
