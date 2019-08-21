from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user

from app.forms.auth import RegisterForm, LoginForm, EmailForm, ResetPasswordForm
from app.forms.movie import UserForm
from app.libs.email import send_email
from app.models.base import db
from app.models.user import User
from . import web

__author__ = '七月'


@web.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        with db.auto_commit():
            user = User()
            user.set_attrs(form.data)
            db.session.add(user)
        return redirect(url_for('web.login'))
    return render_template('auth/register.html',form = form)


@web.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == "POST" and form.validate():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user,remember=True)
            next = request.args.get('next')
            if not next or not next.startswith('/'):
                next = url_for('web.index')
            return redirect(next)

        else:
            flash('账号或密码错误')
    return render_template('auth/login.html',form=form)


@web.route('/further_information ')
@login_required
def further_information():
    id = current_user.id
    return render_template('')

@web.route('/reset/password', methods=['GET', 'POST'])
def forget_password_request():
    if request.method == 'POST':
        form = EmailForm(request.form)
        if form.validate():
            account_email = form.email.data
            user = User.query.filter_by(email=account_email).first_or_404()
            send_email(form.email.data, '重置你的密码',
                       'email/reset_password', user=user,
                       token=user.generate_token())
            flash('一封邮件已发送到邮箱' + account_email + '，请及时查收')
            return redirect(url_for('web.login'))
    return render_template('auth/forget_password_request.html')


@web.route('/reset/password/<token>', methods=['GET', 'POST'])
def forget_password(token):
    if not current_user.is_anonymous:
        return redirect(url_for('web.index'))
    form = ResetPasswordForm(request.form)
    if request.method == 'POST' and form.validate():
        result = User.reset_password(token, form.password1.data)
        if result:
            flash('你的密码已更新,请使用新密码登录')
            return redirect(url_for('web.login'))
        else:
            return redirect(url_for('web.index'))
    return render_template('auth/forget_password.html')


@web.route('/change/password', methods=['GET', 'POST'])
@login_required
def change_password():
    form = ChangePasswordForm(request.form)
    if request.method == 'POST' and form.validate():
        current_user.password = form.new_password1.data
        db.session.commit()
        flash('密码已更新成功')
        return redirect(url_for('web.personal'))
    return render_template('auth/change_password.html', form=form)

@web.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('web.index'))


@web.route('/modified_information', methods=['GET', 'POST'])
@login_required
def modified_information():
    a = request.args
    user_form = UserForm(request.form)
    user = current_user
    if request.method == "POST" and user_form.validate():
        with db.auto_commit():
            user.set_attrs(user_form.data)
        next = request.args.get('next')
        if not next or not next.startswith('/'):
            next = url_for('web.index')
        return redirect(next)
    return render_template('modified_information.html', user=user,form = user_form)


@web.route('/matcher/<int:matcher_id>/deatil/')
@login_required
def matcher_deatil(matcher_id):
    flash('此功能待开发')
    return redirect(url_for('web.index'))