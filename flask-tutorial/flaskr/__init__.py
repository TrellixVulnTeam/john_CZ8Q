import os

from flask import Flask

from flask_sqlalchemy import SQLAlchemy

from sqlalchemy import Column, Integer, String


def create_app():  

	# test_config=None):
	# create and configure the app

	project_dir = os.path.dirname(os.path.abspath(__file__))
	sqlite_file = "sqlite:///{}".format(os.path.join(project_dir, "flaskr.sqlite"))

	app = Flask(__name__,instance_relative_config=True)
	app.config["SQLALCHEMY_SQLITE_URI"] = sqlite_file

	db = SQLAlchemy(app)

	class Author(db.model):
		__tablename__ = "author"
		id = db.Column(db.Integer, primary_key=True)
		firstname = db.Column(db.String(80), nullable=False)
		lastname = db.Column(db.String(80), nullable=False)
		middlename = db.Column(db.String(80), nullable=False)
		username = db.Column(db.String(80), nullable=False)
		password = db.Column(db.String(80), nullable=False)

		def __init__(self, firstname, lastname, middlename, username, password):
			self.firstname = firstname
			self.lastname = lastname
			self.middlename = middlename
			self.username = username
			self.password = password

		def __repr__(self):
			return '<Author %r>' % self.firstname
			

	
						need to be back					
		if test_config is None:
			# load the instance config, if it exists, when not testing
			app.config.from_pyfile('config.py', silent=True)
		else:
			# load the test config if passed in
			app.config.from_mapping(test_config)

		# ensure the instance folder exists
		try:
			os.makedirs(app.instance_path)
		except OSError:
			pass

		# a simple page that says hello
		@app.route('/hello')
		def hello():
			return 'Hello, World!'

		from flaskr import db
		db.init_app(app)

		from flaskr import auth, blog
		app.register_blueprint(auth.bp)
		app.register_blueprint(blog.bp)

		app.add_url_rule('/', endpoint='index')

	return app