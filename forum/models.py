# from flask.ext.login import LoginManager, login_required, current_user, logout_user, login_user
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
import datetime


db = SQLAlchemy(app)


# OBJECT MODELS
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Text, unique=True)
    password_hash = db.Column(db.Text)
    email = db.Column(db.Text, unique=True)
    image_file = db.Column(db.Text,default='profile.png')
    #admin = db.Column(db.Boolean, default=False, unique=True)
    posts = db.relationship("Post", backref="user")
    comments = db.relationship("Comment", backref="user")


    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text)
    content = db.Column(db.Text)
    comments = db.relationship("Comment", backref="post")
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    subforum_id = db.Column(db.Integer, db.ForeignKey('subforum.id'))
    postdate = db.Column(db.DateTime)
    private = db.Column(db.Boolean, default=False)

    # cache stuff
    lastcheck = None
    savedresponce = None

    def __init__(self, title, content, postdate, private):
        self.title = title
        self.content = content
        self.postdate = postdate
        self.private = private

    def get_time_string(self):
        # this only needs to be calculated every so often, not for every request
        # this can be a rudamentary chache
        now = datetime.datetime.now()
        if self.lastcheck is None or (now - self.lastcheck).total_seconds() > 30:
            self.lastcheck = now
        else:
            return self.savedresponce

        diff = now - self.postdate

        seconds = diff.total_seconds()
        print(seconds)
        if seconds / (60 * 60 * 24 * 30) > 1:
            self.savedresponce = " " + str(int(seconds / (60 * 60 * 24 * 30))) + " months ago"
        elif seconds / (60 * 60 * 24) > 1:
            self.savedresponce = " " + str(int(seconds / (60 * 60 * 24))) + " days ago"
        elif seconds / (60 * 60) > 1:
            self.savedresponce = " " + str(int(seconds / (60 * 60))) + " hours ago"
        elif seconds / (60) > 1:
            self.savedresponce = " " + str(int(seconds / 60)) + " minutes ago"
        else:
            self.savedresponce = "Just a moment ago!"

        return self.savedresponce


class Subforum(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, unique=True)
    description = db.Column(db.Text)
    subforums = db.relationship("Subforum")
    parent_id = db.Column(db.Integer, db.ForeignKey('subforum.id'))
    posts = db.relationship("Post", backref="subforum")
    path = None
    hidden = db.Column(db.Boolean, default=False)

    def __init__(self, title, description):
        self.title = title
        self.description = description


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    postdate = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    post_id = db.Column(db.Integer, db.ForeignKey("post.id"))
    # Add parent key

    ####### Madhavi ########
    comments = db.relationship("Comment")  # relates to
    parent_comment_id = db.Column(db.Integer, db.ForeignKey('comment.id'), default=None)
    ####### Madhavi ########

    lastcheck = None
    savedresponce = None

    ### Allen added instance attributes
    def __init__(self, content, postdate, user_id, post_id, parent_comment_id=None):
        self.content = content
        self.postdate = postdate
        self.user_id = user_id
        self.post_id = post_id
        self.parent_comment_id = parent_comment_id

    def get_time_string(self):
        # this only needs to be calculated every so often, not for every request
        # this can be a rudamentary chache
        now = datetime.datetime.now()
        if self.lastcheck is None or (now - self.lastcheck).total_seconds() > 30:
            self.lastcheck = now
        else:
            return self.savedresponce

        diff = now - self.postdate
        seconds = diff.total_seconds()
        if seconds / (60 * 60 * 24 * 30) > 1:
            self.savedresponce = " " + str(int(seconds / (60 * 60 * 24 * 30))) + " months ago"
        elif seconds / (60 * 60 * 24) > 1:
            self.savedresponce = " " + str(int(seconds / (60 * 60 * 24))) + " days ago"
        elif seconds / (60 * 60) > 1:
            self.savedresponce = " " + str(int(seconds / (60 * 60))) + " hours ago"
        elif seconds / (60) > 1:
            self.savedresponce = " " + str(int(seconds / 60)) + " minutes ago"
        else:
            self.savedresponce = "Just a moment ago!"
        return self.savedresponce


db.create_all()