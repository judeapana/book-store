from flask_login import LoginManager
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_toastr import Toastr

migrate = Migrate()
db = SQLAlchemy()
login = LoginManager()
toastr = Toastr()
ma = Marshmallow()
login_manager = LoginManager()
