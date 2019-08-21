# _*_ coding: utf-8 _*_
from app.models.base import db
from app.models.movie import Movie
from app.spider.movie_spider import Movie_spider
from app.view_model.view_movie import MovieCollection

__author__ = 'john'



def set_movie():
    movie_spider = Movie_spider('in_theaters')
    movie_collection = MovieCollection()
    movie_collection.fill(movie_spider)
    with db.auto_commit():
        movie = Movie()
        movie.set_attrs(movie_collection.movies[0].__dict__)

set_movie()