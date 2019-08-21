# _*_ coding: utf-8 _*_
from flask_login import current_user

from app.libs.unums import Group_status
from app.models.user import User

__author__ = 'john'


class GroupViewModel:

    @classmethod
    def grouping(cls,groups):
        returned = []
        for group in groups:
            if group.man_match_id == current_user.id:
                you_are = User.query.filter_by(id = group.women_match_id).first()
            else:
                you_are = User.query.filter_by(id = group.man_match_id).first()
            group_status = Group_status.group_status_str(group.group_status)
            r = {
                'group_id': group.id,
                'you_are': you_are,
                'movie_title': group.movie.title,
                'movie_directors': group.movie.directors,
                'movie_images':group.movie.images,
                'date': group.create_datetime.strftime('%Y-%m-%d'),
                'district': group.movie_mainland_pubdate,
                'status_str': group_status,
            }
            returned.append(r)
        return returned