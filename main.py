from flask import *
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///TODO.db"
db = SQLAlchemy(app)


class Task(db.Model):
    id = db.Column(db.Integer, primary_key = True) 
    name = db.Column(db.String(100), nullable = True)
    txt = db.Column(db.Text)
    priory = db.Column(db.Integer, default = 1)
    collaps_help = db.Column(db.String(50), nullable = True)
    

@app.route('/')
def index():
    tasks = Task.query.all()
    return render_template("index.html", tasks=tasks)

@app.route('/add_task', methods=['GET', 'POST'])
def add_task():
    if request.method == 'POST':
        name = request.form.get('name')
        text = request.form.get('text')
        priority = request.form.get('priority')
        task = Task(name = name, txt = text, priory= priority, collaps_help = 'Three' )
        db.session.add(task)
        db.session.commit()

    return render_template("add_task.html")


@app.route('/delete/<task_number>', methods=['GET', 'POST'])
def delete(task_number):
    task = Task.query.filter_by(id=task_number).delete()
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/update/<task_number>', methods=['GET', 'POST'])
def update(task_number):
    task = Task.query.get(task_number)
    return task.name
   

# with app.app_context():
    # db.create_all()
    # task = Task(name = "покормить кота", collaps_help='One')
    # task = Task(name = "полить цветы", collaps_help='Two')
    # db.session.add(task)
    # db.session.commit()

app.run(debug=True)






