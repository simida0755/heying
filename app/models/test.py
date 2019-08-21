# _*_ coding: utf-8 _*_
from sqlalchemy import Column, Integer, String

from app.models.base import Base

__author__ = 'john'

class User2(Base):
    id = Column(Integer, primary_key=True)
    gender = Column(String(4), default='男')
    nickname = Column(String(24), nullable=False)
