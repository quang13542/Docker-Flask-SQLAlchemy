from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object("flask_project.config.Config")
db = SQLAlchemy(app)


class Author(db.Model):
    __tablename__ = "authors"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128), unique=True, nullable=True)
    active = db.Column(db.Boolean(), default=True, nullable=True)

    def __init__(self, email):
        self.email = email

class Book(db.Model):
    __tablename__ = "books"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128),unique=True, nullable=False)

    author_id = db.Column(db.Integer, db.ForeignKey('authors.id'),
        nullable=False)
    author = db.relationship('Author',
        backref=db.backref('books', lazy=True))

@app.route("/")
def hello_world():
    return jsonify(hello="world")

@app.route("/get")
def get_author():
    author = Author.query.first()
    return jsonify(mail=author.email)

@app.route("/delete")
def delete_author():
    try:
        db.session.delete(Author.query.first())
        db.session.commit()
    except:
        return jsonify(add="fail")
    return jsonify(add="success")

@app.route("/add")
def add_author():
    try:
        db.session.add(Author(email="me@mail.com"))
        db.session.commit()
        print(len(Author.query.all()))
    except:
        return jsonify(add="exist")
    return jsonify(add="success")