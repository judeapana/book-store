from flask import render_template, flash, redirect, request, url_for
from flask_login import login_user

from app.auth.forms import LoginForm
from app.auth.views import auth
from app.models import User
from app.utils import InvalidAuthentication


@auth.route('/', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        password = form.password.data
        username = form.username.data.strip()
        user = User.query.filter(
            (User.username == username) | (User.email_address == username)).first()
        try:
            if not user:
                raise InvalidAuthentication('Incorrect Username or Password')
            else:
                if user.password != password:
                    raise InvalidAuthentication('Incorrect Username or Password')
                else:
                    login_user(user, remember=form.remember_me.data)
                    return redirect(url_for('admin.dashboard'))

        except InvalidAuthentication as e:
            flash(str(e), 'error')
            return redirect(request.url)
    return render_template('auth/pages/login.html', form=form, title='BOOK APP')
