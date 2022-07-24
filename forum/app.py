from flask import Flask
from os.path import join, dirname, realpath

app = Flask(__name__)
app.config.update(
	# APP_ROOT=os.path.dirname(os.path.abspath(__file__)),
	UPLOAD_FOLDER=join(dirname(realpath(__file__)), 'static/uploads/'),
	TESTING=True,
	SECRET_KEY=b'kristofer',
	SITE_NAME = "Hawaiian Shirt Party",
	SITE_DESCRIPTION = "a forum for Hawaiian Shirt Enthusiasts",
	SQLALCHEMY_DATABASE_URI='sqlite:////tmp/database.db'

)
