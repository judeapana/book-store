from flask import Blueprint

from app.models import User

auth = Blueprint('auth', __name__, template_folder='templates', url_prefix='/auth')

from app.auth.views import login, logout


@auth.before_request
def create_user():
    user = User.query.filter(User.username == 'admin', User.email_address == 'admin@boo.com').first()
    if not user:
        user = User(username='admin',
                    password='admin',
                    email_address='admin@boo.com',
                    phone_number='0554138989')
        user.save()
