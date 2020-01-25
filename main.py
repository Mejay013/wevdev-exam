from flask import Blueprint , render_template , url_for , redirect , request
from .models import Appeal,Appeal_type, Appeal_status, User , Role
from flask_login import current_user
from .app import db
import datetime

main = Blueprint('main',__name__)

@main.route('/')
def index():
    appeal_list = Appeal.query.all()
    type_appeal = Appeal_type
    appeal_status = Appeal_status
    user = User
    role = Role
    return render_template('index.html',appeal_list=appeal_list,type_appeal=type_appeal,appeal_status=appeal_status,user=user,role=role)

@main.route('/set/<id>')
def set(id):
    type_appeal = Appeal_type
    appeal_status = Appeal_status
    user = User
    role = Role
    return render_template('set.html',appeal=appeal,type_appeal=type_appeal,appeal_status=appeal_status,user=user,role=role)

@main.route('/add_appeal')
def add_appeal():
    if request.method == "POST":
        appeal_user = current_user.id
        appeal_type = request.form['appeal_type']
        appeal_message = request.form['appeal_message']
        date = datetime.datetime.now()
        new_appeal = Appeal(login=login , user=appeal_user , password=generate_password_hash(password,method='sha256'),role = 3)
    else:
        type_appeal = Appeal_type
        appeal_status = Appeal_status
        user = User
        role = Role
        return render_template('app.html',type_appeal=type_appeal,appeal_status=appeal_status,user=user,role=role)
