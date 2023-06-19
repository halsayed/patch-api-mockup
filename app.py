import os
from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from config import config
from forms import TaskCreate
from flask_sqlalchemy import SQLAlchemy
from flask_restful import reqparse, abort, Api, Resource

app_config = config[os.getenv('FLASK_ENV') or 'default']
app = Flask(__name__)
app.config.from_object(app_config)
api = Api(app)
db = SQLAlchemy(app)
bootstrap = Bootstrap(app)

from models import Todo, Machines, Patches

db.create_all()

parser = reqparse.RequestParser()
parser.add_argument('task')


@app.route('/', methods=['GET', 'POST'])
def dashboard():
    form = TaskCreate()
    if form.is_submitted():
        new_task = Todo(name=form.name.data,
                        description=form.description.data)
        db.session.add(new_task)
        db.session.commit()
    tasks = Todo.query.all()

    return render_template('dashboard.jinja2',
                           ip_address=request.host[:request.host.find(':')],
                           version=app_config.VERSION,
                           tasks=tasks,
                           form=form)


if __name__ == '__main__':
    app.run()
