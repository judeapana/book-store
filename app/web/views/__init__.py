from flask import Blueprint, render_template

web = Blueprint('web', __name__, template_folder='templates', url_prefix='/')


@web.route('/')
def index():
    return render_template('web/index.html')
