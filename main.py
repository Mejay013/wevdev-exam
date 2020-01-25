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

@main.route('/set/<id>',methods=['POST','GET'])
def set(id):
    if request.method == 'POST':
        bad_appeal= Appeal.query.filter_by(id=id).first()

        user_fio = request.form['red_user_fio']
        appeal_user = User.query.filter_by(user_fio= user_fio).first().id
        new_appeal_type = request.form['red_appeal_type']
        new_appeal_status = request.form['red_appeal_status']
        new_message = request.form['new_message']
        appeal_date = datetime.datetime.now()

        if not bad_appeal:
            type_appeal = Appeal_type
            appeal_status = Appeal_status
            user = User
            role = Role
            error = "Изменения уже приступили в силу"
            return render_template('app.html',type_appeal=type_appeal,appeal_status=appeal_status,user=user,role=role,error=error)
        db.session.delete(bad_appeal)
        red_appeal = Appeal(date=appeal_date , user=appeal_user ,type_appeal=new_appeal_type,status_appeal=new_appeal_status ,message_appeal = new_message)
        db.session.add(red_appeal)
        db.session.commit()
        return render_template('index.html')
    else:
        appeal = Appeal.query.filter_by(id = id).first()
        type_appeal = Appeal_type
        appeal_status = Appeal_status
        user = User
        role = Role
        return render_template('set.html',appeal=appeal,type_appeal=type_appeal,appeal_status=appeal_status,user=user,role=role)

@main.route('/delete/<id>',methods=['POST','GET'])
def delete(id):
    bad_appeal = Appeal.query.filter_by(id=id).first()
    if not bad_appeal:
        return redirect(url_for('main.index'))
    db.session.delete(bad_appeal)
    db.session.commit()
    return redirect(url_for('main.index'))

@main.route('/add_appeal',methods=['POST','GET'])
def add_appeal():
    if request.method == "POST":
        appeal_user = current_user.id
        appeal_type = request.form['appeal_type']
        appeal_message = request.form['appeal_message']
        appeal_date = datetime.datetime.now()

        check_message =  Appeal.query.filter_by(message_appeal = appeal_message).first()
        if check_message:
            type_appeal = Appeal_type
            appeal_status = Appeal_status
            user = User
            role = Role
            error = "Обращение уже существует"
            return render_template('app.html',type_appeal=type_appeal,appeal_status=appeal_status,user=user,role=role,error=error)

        new_appeal = Appeal(date=appeal_date , user=appeal_user ,type_appeal=appeal_type,status_appeal=1 ,message_appeal = appeal_message)

        db.session.add(new_appeal)
        db.session.commit()
        return render_template('index.html')
    else:
        type_appeal = Appeal_type
        appeal_status = Appeal_status
        user = User
        role = Role
        return render_template('app.html',type_appeal=type_appeal,appeal_status=appeal_status,user=user,role=role)
