# _*_ coding: utf-8 _*_
from sqlalchemy import Integer, Column, String, ForeignKey
from sqlalchemy.orm import relationship

from app.models.base import Base

__author__ = 'john'


class MovieSubjoin(Base):
    __tablename__ = 'moviesubjoin'
    # id
    id = Column(Integer,primary_key=True,autoincrement=True)
    # 唯一编号
    mid = Column(Integer, ForeignKey('movie.mid'), nullable=False)
    movie = relationship('Movie')
    # tag_正在上映，即将上映，下架
    keyword = Column(String(20))

    @classmethod
    def mid_list(cls,keyword = ''):
        if keyword == '':
            return [movie.mid for movie in cls.query.all()]
        else:
            return [movie.mid for movie in cls.query.filter_by(keyword = keyword)]

