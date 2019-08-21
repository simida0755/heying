# _*_ coding: utf-8 _*_
from flask import current_app
from flask_login import UserMixin
from sqlalchemy import Column, Integer, String, Boolean, Float
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

from app import login_manager

from app.models.base import Base, db

__author__ = 'john'


class User(UserMixin,Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    gender = Column(String(4), default='男')
    nickname = Column(String(24), nullable=False)
    name = Column(String(24))
    phone_number = Column(String(18))
    email = Column(String(50), unique=True, nullable=False)
    _password = Column('password', String(128), nullable=False)
    confirmed = Column(Boolean, default=False)
    send_counter = Column(Integer, default=0)
    receive_counter = Column(Integer,default=0)
    image = Column(String(300))
    district = Column(String(20))
    subway_site = Column(String(20))
    matchs = relationship('Match')
    # group_message = Column(String(24))



    def generate_token(self, expiration=600):
        s = Serializer(current_app.config['SECRET_KEY'], expiration)
        return s.dumps({'id': self.id}).decode('utf-8')

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self,raw):
        self._password = generate_password_hash(raw)

    def check_password(self,raw):
        return check_password_hash(self._password,raw)

    @property
    def group_sex(self):
        return '女' if self.gender == '男' else '男'


    @property
    def can_save_macth_or_group(self):
        if self.phone_number and self.district:
            return True
        else:
            return False

    @staticmethod
    def reset_password(token, new_password):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token.encode('utf-8'))
        except:
            return False
        user = User.query.get(data.get('id'))
        if user is None:
            return False
        user.password = new_password
        db.session.commit()
        return True


@login_manager.user_loader
def get_user(uid):
    return User.query.get(int(uid))

