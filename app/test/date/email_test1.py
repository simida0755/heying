import os
from flask import Flask
from flask_script import Manager
from flask_mail import Mail, Message


app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.163.com'
app.config['MAIL_PORT'] = 25
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'simida0755@sina.com'
app.config['MAIL_PASSWORD'] = '623011562'

#
# MAIL_SERVER = 'smtp.sina.com'
# MAIL_PORT = 25
# MAIL_USE_SSL = False
# MAIL_USE_TLS = True
# MAIL_USERNAME = 'simida0755@sina.com'
# MAIL_PASSWORD = '623011562'

manager = Manager(app)
mail = Mail(app)

if __name__ == '__main__':
    manager.run()