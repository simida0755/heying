# _*_ coding: utf-8 _*_
from flask_login import current_user
from sqlalchemy import Column, Integer, ForeignKey, String, or_
from sqlalchemy.orm import relationship

from app.libs.unums import Group_status
from app.models.base import Base
from app.models.match import Match
from app.models.user import User

__author__ = 'john'


class Group(Base):
    __tablename__ = 'group'
    def __init__(self):
        self.group_status = Group_status.wait_watch
        super(Group, self).__init__()

    id = Column(Integer, primary_key=True, autoincrement=True)
    man_match_id = Column(Integer,nullable=False)
    women_match_id = Column(Integer, nullable=False)
    man_nickname = Column(String(24), nullable=False)
    women_nickname = Column(String(24), nullable=False)
    district = Column(String(20))
    mid = Column(Integer, ForeignKey('movie.mid'), nullable=False)
    movie = relationship('Movie')
    movie_mainland_pubdate = Column(String(50))
    _group_status = Column('group_status',Integer, default=1)

    @property
    def group_status(self):
        return Group_status(self._group_status)

    @group_status.setter
    def group_status(self, status):
        self._group_status = status.value

    @property
    def group_status_str(self):
        return Group_status.group_status_str(self.group_status)

    @staticmethod
    def find_group_matcher(user,movie):
        if Group.has_in_group(user,movie):
            return False
        match = Match.query.filter_by(
            matcher_gender = user.group_sex,
            matcher_district = user.district,mid = movie.mid).first()
        return match if match else False

    @staticmethod
    def has_in_group(user,movie):
        if Group.query.filter(
                or_(Group.women_match_id == user.id,Group.man_match_id == user.id),
                Group.mid == movie.mid,Group.status == 1,Group._group_status == Group_status.wait_watch.value).first():
            return True
        else:
            return False


    @property
    def current_user_grouper(self):
        if current_user.gender == '男':
            return User.query.filter_by(id = self.women_match_id).first()
        else:
            return User.query.filter_by(id = self.man_match_id).first()

    @classmethod
    def mid_list(cls,status):
        groups = cls.query.filter_by(_group_status = status).all()
        mid_list = [group.mid for group in groups]
        return mid_list

    # @property
    # def current_user_grouper(self):
    #     if current_user:
    #         if current_user.gender == '男':
    #             return User.query.filter_by(id=self.women_match_id).first()
    #         else:
    #             return User.query.filter_by(id=self.man_match_id).first()
    #     else:
    #         return None