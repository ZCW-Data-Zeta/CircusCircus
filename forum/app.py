from flask import Flask


app = Flask(__name__)
app.config.update(
	UPLOAD_FOLDER ="static/uploads/",
	TESTING=True,
	SECRET_KEY=b'kristofer',
	SITE_NAME = "Hawaiian Shirt Party",
	SITE_DESCRIPTION = "a forum for Hawaiian Shirt Enthusiasts",
	SQLALCHEMY_DATABASE_URI='sqlite:////tmp/database.db'

)
