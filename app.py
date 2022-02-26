# RUN `virtualenv -p python3 venv` before working on app

from flask import Flask, render_template, request, redirect, url_for
from forms import Todo, rmTodo
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'password'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tmp/test.db'
db = SQLAlchemy(app)


class TodoModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(240))

    def __str__(self):
        return f'{self.content}, {self.id}'


@app.route('/', methods=['GET', 'POST'])
def index():

    request_method = request.method
    todo = TodoModel.query.all()

    return render_template('index.html', request_method=request_method, todo=todo)


@app.route('/todo', methods=['GET', 'POST'])
def todo():
    todo_form = Todo()
    if todo_form.validate_on_submit():
        todo = TodoModel(content=todo_form.content.data)
        db.session.add(todo)
        db.session.commit()
        return redirect('/')
    return render_template('todo.html', form=todo_form)


@app.route('/rmtodo', methods=['GET', 'POST'])
def rmtodo():
    todo_form = rmTodo()
    if todo_form.validate_on_submit():
        todo = TodoModel(content=todo_form.content.data)
        db.session.query(TodoModel).filter(
            TodoModel.id == int(todo.content)).delete(synchronize_session=False)
        db.session.commit()
        return redirect('/')
    return render_template('rmtodo.html', form=todo_form)


if __name__ == '__main__':  # If executed directly, run Flask server
    app.run(debug=True)
