# _*_ coding: utf-8 _*_
from app.libs.unums import Match_status, Group_status
from app.models.base import db
from app.models.group import Group
from app.models.match import Match
from app.models.movie import Movie
from app.models.movie_subjoin import MovieSubjoin

__author__ = 'john'

class Updata_database:

    @staticmethod
    def update_movie(movie_view):
        mid_list = [movie.mid for movie in Movie.all_movie()]
        for a_movie in movie_view.movies:
            if int(a_movie.mid) in mid_list:
                continue
            with db.auto_commit():
                movie = Movie()
                movie.set_attrs(a_movie.__dict__)
                db.session.add(movie)

    @staticmethod
    def update_movie_subjoin(movie_view):
        try:
            for movie in MovieSubjoin.query.all():
                with db.auto_commit():
                    db.session.delete(movie)
            for movie in movie_view.movies:
                movie_subjoin = MovieSubjoin()
                with db.auto_commit():
                    movie_subjoin.keyword = movie.keyword
                    movie_subjoin.mid = movie.mid
                    db.session.add(movie_subjoin)
        except Exception as e:
            db.session.rollback()
            raise e




    @staticmethod
    def update_match():
        movie_mid_list = Movie.mid_list()
        match_wait_mid_list = Match.mid_list(Match_status.wait_match.value)
        de_mid_list = list(set(match_wait_mid_list) - set(movie_mid_list))
        matches = Match.query.filter(Match.mid.in_(de_mid_list),
                                     Match._match_status == Match_status.wait_match.value).all()
        if matches:
            for match in matches:
                with db.auto_commit():
                    match.match_status = Match_status.cancel_match

    @staticmethod
    def update_group():
        movie_mid_list = Movie.mid_list()
        group_wait_mid_list = Group.mid_list(Group_status.wait_watch.value)
        de_mid_list = list(set(group_wait_mid_list) - set(movie_mid_list))
        groups = Group.query.filter(Group.mid.in_(de_mid_list),
                                    Group.group_status == Group_status.wait_watch.value).all()

        if groups:
            for group in groups:
                with db.auto_commit():
                    group.group_status = Group_status.cancel_watch
