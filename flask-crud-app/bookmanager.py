import os

from flask import Flask
from flask import request, redirect, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "bookdatabase.db"))

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = database_file

db = SQLAlchemy(app)

class Author(db.Model):
    __tablename__ = "author"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self):
         return '<Author %r>' % self.first_name

# registration class 


class Book(db.Model):
    __tablename__ = "book"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    no_of_pages = db.Column(db.Integer, nullable=False)
    date_published = db.Column(db.Integer, nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'), nullable=False)
    
    author = db.relationship('Author', backref='book')

    def __init__(self, title, no_of_pages, date_published, rating, author_id):
        self.title = title
        self.no_of_pages = no_of_pages
        self.date_published = date_published
        self.rating = rating
        self.author_id = author_id

    def __repr__(self):
        return '<Book %r>' % self.title



@app.route('/')
def index():
    myAuthor = Author.query.all()
    myBook = Book.query.all()
    return render_template('add.html', myAuthor=myAuthor, myBook=myBook)

@app.route('/get_user', methods=["GET", "POST"])
def get_user():
    author = Author(request.form['first_name'], request.form['last_name'])
    db.session.add(author)
    db.session.commit()

    author_id = Author.query.filter_by(first_name=request.form['first_name'],last_name=request.form['last_name']).first()
    author_id = author_id.id


    book = Book(request.form['title'], request.form['no_of_pages'], request.form['date_published'], request.form['rating'], author_id)

    db.session.add(book)
    db.session.commit()



    return redirect(url_for('index'))


# @app.route("/update", methods=["POST"])
# def update():
#     try:
#         newtitle = request.form.get("newtitle")
#         oldtitle = request.form.get("oldtitle")
#         book = Book.query.filter_by(title=oldtitle).first()
#         book.title = newtitle
#         db.session.commit()
#     except Exception as e:
#         print("Couldn't update book title")
#         print(e)
#     return redirect("/")


# @app.route("/delete", methods=["POST"])
# def delete():
#     title = request.form.get("title")
#     book = Book.query.filter_by(title=title).first()
#     db.session.delete(book)
#     db.session.commit()
#     return redirect("/")

db.create_all()

if __name__ == "__main__":
    app.run(debug=True)