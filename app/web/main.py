# _*_ coding: utf-8 _*_
from flask import render_template

from app.libs.unums import In_theaters_status
from app.models.base import db
from app.models.movie import Movie
from app.models.movie_subjoin import MovieSubjoin
from app.service.update_database import Updata_database
from app.spider.movie_spider import Movie_spider
from app.view_model.view_movie import MovieViewCollection
from tomovie import app

__author__ = 'john'


from app.web import web

@web.route('/')
def index():
    mid_list = MovieSubjoin.mid_list(app.config['MOVIE_KEYWORD']['set_movie']['in_theaters'])
    movie = Movie.query.filter(Movie.mid.in_(mid_list)).all()
    return render_template('index.html',recent=movie)

@web.route('/coming_soon')
def coming_soon():
    mid_list = MovieSubjoin.mid_list(app.config['MOVIE_KEYWORD']['set_movie']['coming_soon'])
    movie = Movie.query.filter(Movie.mid.in_(mid_list)).all()
    return render_template('index.html',recent=movie)


@web.route('/set_movie')
def set_movie():
    movie_view_collection = MovieViewCollection()
    for keyword in app.config['MOVIE_KEYWORD']['set_movie'].values():
        movie_view_collection.fill(Movie_spider(keyword))
    Updata_database.update_movie(movie_view_collection)
    print('更新电影')
    Updata_database.update_movie_subjoin(movie_view_collection)
    Updata_database.update_match()
    Updata_database.update_group()
    return 'set movie success'

@web.route('/half_index')
def half_index():
    return 'half'

@web.route('/personal_center')
def personal_center():
    pass