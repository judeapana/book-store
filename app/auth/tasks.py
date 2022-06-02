from enum import Enum
from uuid import uuid4

from flask import render_template
from flask_mail import Message

from uni import mail, rq


@rq.job(description="Confirm mail", func_or_queue="uni_default")
def send_confirmation_email(email, link, template='auth/mail/confirm_account_email.html'):
    unique = str(uuid4)

    try:
        message = Message()
        message.recipients = [email]
        message.subject = f'DHLTU MIS ({unique})'
        message.html = render_template(template, link=link)
        mail.send(message)
    except Exception as e:
        return e


@rq.job(description="Forgot password", func_or_queue="uni_default")
def send_forgot_reset_password(email, link, template='auth/mail/forgot_password.html'):
    unique = str(uuid4)
    try:
        message = Message()
        message.recipients = [email]
        message.subject = f'DHLTU MIS Forgot Password ({unique})'
        message.html = render_template(template, link=link)
        mail.send(message)
    except Exception as e:
        return e


@rq.job(description="sending credentials", func_or_queue="uni_default")
def send_credentials(email, link, username, password, template='auth/mail/send_credentials.html'):
    unique = str(uuid4)
    try:
        message = Message()
        message.recipients = [email]
        message.subject = f'DHLTU MIS Account Activation ({unique})'
        message.html = render_template(template, link=link, username=username, password=password)
        mail.send(message)
    except Exception as e:
        return e


class ContentTypeEnum(Enum):
    HTML = 1
    TEXT = 2


@rq.job(description='Sending email', func_or_queue='uni_default')
def send_email(email, msg, content_type: ContentTypeEnum = ContentTypeEnum.TEXT, subject=None, allow_support=False):
    unique = str(uuid4)
    try:
        message = Message()
        if email:
            message.recipients = [email]
        else:
            message.recipients = ['limannmis@gmail.com']
        if subject is not None:
            message.subject = subject
        else:
            message.subject = f'MIS Support Team ({unique})'
        if content_type == ContentTypeEnum.TEXT:
            message.body = msg
        if content_type == ContentTypeEnum.HTML:
            message.html = msg
        message.cc = ['limannmis@gmail.com']
        if allow_support:
            message.cc.append('techsupport@dhltu.edu.gh')
        mail.send(message)
    except Exception as e:
        return e
