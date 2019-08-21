# _*_ coding: utf-8 _*_
from flask import current_app

from app.libs.httper import HTTP
from app.view_model.movie import MovieViewModel

__author__ = 'john'


class Movie_spider:
    base_url = 'http://api.douban.com/v2/movie/{}?apikey={}&start={}&count={}'
    APIKEY = '0df993c66c0c636e29ecbb5344252a4a'
    PER_PAGE = 100


    def __init__(self,keyword):
        self.total = 0
        self.movies = []
        self.in_theaters_status = keyword
        self.get_all_movies()

    def get_all_movies(self):
        self.get_movies(self.in_theaters_status)
        if self.need_get_count() > 1:
            page = 1
            for i in range(self.need_get_count()):
                page += 1
                self.get_movies(self.in_theaters_status,page= page)

    def get_movies(self,keyword,page=1):
        url = self.base_url.format(keyword,self.APIKEY,self.calulate_start(page),self.PER_PAGE)
        result = HTTP.get(url)
        return self.__fill_collection(result)

    def __fill_collection(self,data,):
        if data:
            self.total = data['total']
            self.movies = self.movies + data['subjects']

    def calulate_start(self,page):
        return (page - 1) * self.PER_PAGE


    def need_get_count(self):
        return self.total // self.PER_PAGE




