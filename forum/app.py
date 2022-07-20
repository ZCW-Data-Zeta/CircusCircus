from flask import Flask

app = Flask(__name__)
app.config.update(
    TESTING=True,
    SECRET_KEY='kristofer',
	SITE_NAME = "Schooner",
	SITE_DESCRIPTION = "a schooner forum",
	SQLALCHEMY_DATABASE_URI='sqlite:////tmp/database.db'
	# COPYRIGHT = "ZIP CODE DATA ZETA 3.1 © 2022"
)
