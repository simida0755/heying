# # _*_ coding: utf-8 _*_
# from flask import Flask
#
# __author__ = 'john'
#
# from flask_script import Manager
#
# from flask_migrate import Migrate,MigrateCommand
# from app.models.base import db
#
#
#
# app = Flask(__name__)
# app.config.from_object('app.config.migrate_secure')
#
#
# manager = Manager(app = app)
#
# # init migrate upgrade
# # 模型 ->迁移文件 ->表
# # 1.要使用flask_migrate，必须绑定app和 DB
# migrate = Migrate(app,db)
#
# # 2.把migrateCommand命令添加到manager中
# manager.add_command('db',MigrateCommand)
# from app.models import base,user,match,group,movie
#
# if __name__=='__main__':
#     manager.run()
