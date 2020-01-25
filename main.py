from flask import Blueprint , render_template , url_for , redirect , request
from .models import Appeal,Appeal_type, Appeal_status, User , Role
from .app import db
main = Blueprint('main',__name__)

@main.route('/')
def index():
    appeal_list = Appeal.query.all()
    type_appeal = Appeal_type
    appeal_status = Appeal_status
    user = User
    role = Role
    return render_template('index.html',appeal_list=appeal_list,type_appeal=type_appeal,appeal_status=appeal_status,user=user,role=role)
