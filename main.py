from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Referencing this file
app = Flask(__name__)
# Database connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
# Initialize database
db  = SQLAlchemy(app)

# ORM Model creation
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.Date, default=datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' % self.id


# Routing
@app.route('/')
def index():
    return render_template('index.html')

# Running server
if __name__ == '__main__':
    app.run(debug=True)