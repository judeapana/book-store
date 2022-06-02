from flask import Flask

from app.config import LocalConfig
from app.ext import migrate, login, toastr, ma, login_manager
from app.models import db


def create_app(conf=LocalConfig):
    app = Flask(__name__)
    app.config.from_object(conf)
    db.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)
    toastr.init_app(app)
    ma.init_app(app)
    app.register_blueprint(admin)
    app.register_blueprint(web)
    app.register_blueprint(auth)

    return app


from app.admin.views import admin
from app.web.views import web
from app.auth.views import auth
