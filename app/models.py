from flask_login import UserMixin
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy_utils import PasswordType, PhoneNumberType

from app.ext import db, login_manager
from app.utils import ActiveRecord


@login_manager.user_loader
def load_user(pk):
    return User.query.get(pk)


class User(db.Model, ActiveRecord, UserMixin):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    username = db.Column(db.String(50), nullable=False, info={'label': 'Username'}, unique=True, )
    password = db.Column(PasswordType(max_length=255, schemes=['pbkdf2_sha512']), nullable=False, )
    email_address = db.Column(db.String(50), nullable=True, info={'label': 'Email Address'}, )
    phone_number = db.Column(PhoneNumberType(region='GH'), info={'label': 'Phone Number'}, nullable=True)
    last_logged_in = db.Column(db.DateTime)


class Book(db.Model, ActiveRecord):
    id = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
    title = db.Column(db.Text, nullable=False, unique=True)
    isbn = db.Column(db.Text, nullable=True, unique=True)
    description = db.Column(db.Text, nullable=True)
    year = db.Column(db.Integer, nullable=True)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id', ondelete='cascade'), nullable=False)
    genre_id = db.Column(db.Integer, db.ForeignKey('genre.id', ondelete='cascade'), nullable=False)


class Author(db.Model, ActiveRecord):
    id = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=True)
    middle_name = db.Column(db.String(100), nullable=True)
    books = db.relationship('Book', backref=db.backref('author'), cascade='all,delete,delete-orphan',
                            lazy='dynamic')

    @hybrid_property
    def full_name(self):
        return f'{self.first_name} {self.last_name} {self.middle_name}'


class Genre(db.Model, ActiveRecord):
    id = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    description = db.Column(db.Text, nullable=True)
    books = db.relationship('Book', backref=db.backref('genre'), cascade='all,delete,delete-orphan',
                            lazy='dynamic')
