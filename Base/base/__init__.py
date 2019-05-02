from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    db.init_app(app)
    return app

login_manager = LoginManager(app)


@app.route("/")
@app.route("/layout")
def layout():
	# posts = Post.query.all()
	
	return render_template('layout.html')

@app.route("/login", methods=['GET'])#next ids for db commit
def login():
	 	# db.session.add(user)
		# db.session.commit()
		# flash('Your account has been created! You are now able to log in', 'success')
		# return redirect(url_for('login'))
	return render_template('login.html', title='LOGIN')

@app.route("/register")
def register():
	user = User(username=form.username.data, email=form.email.data, password=hashed_password)
		# db.session.add(user)
		# db.session.commit()
		# flash('Your account has been created! You are now able to log in', 'success')
		# return redirect(url_for('login'))
	return render_template('register.html', title='Register')

@app.route("/profile")
def profile():

	return render_template('profile.html', title='Profile')