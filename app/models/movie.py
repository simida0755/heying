# _*_ coding: utf-8 _*_
from datetime import datetime

from flask_login import current_user
from sqlalchemy import Column, String, Integer, Float, SmallInteger
from sqlalchemy.testing import db

from app.models.base import Base

__author__ = 'john'

class Movie(Base):
    __tablename__ = 'movie'
    # id
    id = Column(Integer,primary_key=True,autoincrement=True)
    # 唯一编号
    mid = Column(Integer,nullable=False, unique=True)
    # 图片
    images = Column(String(300))
    # 片名
    title = Column(String(50),nullable=False)
    # 导演
    directors = Column(String(300),default='')
    # 类型
    genres = Column(String(50))
    # 主演
    casts = Column(String(50))
    # 片长
    durations = Column(String(50))
    # 上映时间
    mainland_pubdate = Column('mainland_pubdate',String(50))
    # 制片国家与地区
    pubdates = Column(String(300))
    # 豆瓣评分
    average = Column(Float)

    def string_is_time_standard(self):
        # 判断存储的时间字符串是否为标准格式
        if not self.mainland_pubdate:
            return False
        try:
            datetime.strptime(self.mainland_pubdate, "%Y-%m-%d")
        except Exception as e :
            return False
        return True


    def movie_not_sold_out(self):

        if self.mainland_pubdate:
            pass

    @classmethod
    def all_movie(cls):
        return cls.query.all()

    @classmethod
    def mid_list(cls):
        return [movie.mid for movie in Movie.all_movie()]

