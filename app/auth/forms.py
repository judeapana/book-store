from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired


class LoginForm(FlaskForm):
    username = StringField('User ID', validators=[InputRequired()], render_kw={'autofocus': True})
    password = PasswordField('Password', validators=[InputRequired()])
    remember_me = BooleanField('Remember Me')
