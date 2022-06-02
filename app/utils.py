from flask import flash
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy_utils import Timestamp

from app.ext import db


class InvalidAuthentication(Exception):
    """
    Login Exception
    """
    pass


class ActiveRecord(Timestamp):
    def save(self, **kwargs):
        try:
            db.session.add(self)
            db.session.commit()
            if kwargs.get('message'):
                flash(kwargs.get('message'), 'success')
            return True
        except SQLAlchemyError as e:
            db.session.rollback()
            flash('Unable to complete task', 'error')
            print(e)
            return False

    def delete(self, **kwargs):
        try:
            db.session.delete(self)
            db.session.commit()
            if kwargs.get('message'):
                flash(kwargs.get('message'), 'success')
        except SQLAlchemyError as e:
            print(e)
            db.session.rollback()
            flash('Error Occurred, maybe it has multiple references to other entries. Please delete them and try again',
                  'error')
