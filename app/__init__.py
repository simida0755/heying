# _*_ coding: utf-8 _*_
from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from app.libs.email import mail
from app.models.base import db

__author__ = 'john'

login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.setting')
    app.config.from_object('app.config.secure')
    register_blueprint(app)
    login_manager.init_app(app)
    login_manager.login_view = 'web.login'
    login_manager.login_message = '请先登录或注册'
    mail.init_app(app)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    # manager = Manager(app)
    #
    # # init migrate upgrade
    # # 模型 ->迁移文件 ->表
    # # 1.要使用flask_migrate，必须绑定app和 DB
    # migrate = Migrate(app, db)
    #
    # # 2.把migrateCommand命令添加到manager中
    # manager.add_command('db', MigrateCommand)
    return app


def register_blueprint(app):
    from app.web import web
    app.register_blueprint(web)