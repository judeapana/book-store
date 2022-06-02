from flask_wtf import FlaskForm
from wtforms.validators import InputRequired
from wtforms_alchemy import ModelForm, QuerySelectField

from app.models import Author, Book, Genre


class BookForm(ModelForm, FlaskForm):
    class Meta:
        model = Book

    author = QuerySelectField('Author', validators=[InputRequired()], query_factory=lambda: Author.query,
                              get_label='full_name')
    genre = QuerySelectField('Genre', validators=[InputRequired()], query_factory=lambda: Genre.query,
                             get_label='name')


class AuthorForm(ModelForm, FlaskForm):
    class Meta:
        model = Author


class GenreForm(ModelForm, FlaskForm):
    class Meta:
        model = Genre
