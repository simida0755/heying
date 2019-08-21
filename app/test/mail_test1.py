# _*_ coding: utf-8 _*_
from flask_mail import Message

__author__ = 'john'


def send_mail():

    mag = Message('测试邮件', sender = 'xxx@qq.com',body='TEst',
                  recipients=['xxx@qq.com'])