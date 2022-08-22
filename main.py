# Access to the libraries
from flask import Flask, url_for, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


# Turn this file into a web application with Flask
app = Flask(__name__)
# Database connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
# Initialize database
db  = SQLAlchemy(app)


# ORM Model creation
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' % self.id


# Routing
# Listen to the requests
@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        task_content = request.form['content']
        new_task = Todo(content=task_content)

        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue adding yout task'

    else:
        tasks = Todo.query.order_by(Todo.date_created).all() 
        return render_template('index.html', tasks=tasks)


@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete = Todo.query.get_or_404(id)
    
    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return 'There was a problem deleting the task'
    

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    return ''
    

# Running server
if __name__ == '__main__':
    app.run(debug=True)