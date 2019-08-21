# _*_ coding: utf-8 _*_
from sqlalchemy import Column, Integer, ForeignKey, String, Boolean
from sqlalchemy.orm import relationship

from app.libs.unums import Match_status
from app.models.base import Base

__author__ = 'john'


class Match(Base):
    __tablename__ = 'match'

    def __init__(self):
        self.match_status = Match_status.wait_match
        super(Match, self).__init__()

    id = Column(Integer, primary_key=True, autoincrement=True)
    mid = Column(Integer, ForeignKey('movie.mid'), nullable=False)
    movie = relationship('Movie')
    movie_mainland_pubdate = Column(String(50))
    uid = Column(Integer, ForeignKey('user.id'), nullable=False)
    user = relationship('User')
    matcher_gender = Column(String(4), nullable=False)
    matcher_district = Column(String(20))
    matcher_subway_site = Column(String(20))
    launched = Column(Boolean, default=False)
    _match_status = Column('match_status',Integer,default=1)


    @staticmethod
    def has_in_match(user,movie):
        if Match.query.filter_by(uid = user.id,movie = movie,match_status =  Match_status.wait_match.value ).first():
            return True
        else:
            return False

    @property
    def match_status(self):
        return Match_status(self._match_status)

    @match_status.setter
    def match_status(self,status):
        self._match_status = status.value

    @property
    def match_status_str(self):
        return Match_status.match_status_str(self.match_status)

    @classmethod
    def mid_list(cls,status):
        matchs = cls.query.filter_by(_match_status = status).all()
        mid_list = [match.mid for match in matchs]
        return mid_list

