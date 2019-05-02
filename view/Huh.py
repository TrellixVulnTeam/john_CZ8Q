from flask import Flask

app = Flask(__name__)

# @ signifies a decorator - way to wrap a function and modifying its behavior
#@app.route('/')
#return 'This is the home page.'

#@app.route('/tuna')
#def tuna():
#	return '<h2>Tuna is good</h2>'

#@app.route('/profile/<username>')
#def profile(username):
#	return "Hey there %s" % username

#@app.route('/profile/<username>')
#def profile(username):
#	return "<h2>Hey there %s<h2>" % username

@app.route('/post/<int:post_id>')
def post(post_id):   #can also be show_post or what you like to name it
		return "<h2>Post ID is %s</h2>" % post_id

if __name__== "__main__":
	app.run()

	#also knew that it can make a lot of web pages