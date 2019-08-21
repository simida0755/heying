# _*_ coding: utf-8 _*_
from app.spider.movie_spider import Movie_spider

__author__ = 'john'

class MovieViewModel_2:
    def __init__(self,movie):
        self.mid = movie['id']
        self.title = movie['title']
        self.images = movie['images']['small'] if movie['images']['small'] else ''
        self.directors = '/'.join([directors['name'] for directors in movie['directors']])
        self.genres = '/'.join(movie['genres'])if 'genres' in movie.keys() else '未知'
        self.casts = '/'.join([casts['name'] for casts in movie['casts']]) or ''
        self.durations = movie['durations'] if 'durations' in movie.keys() else '未知'
        self.mainland_pubdate = movie['mainland_pubdate']
        self.pubdates = movie['pubdates']
        self.average = movie['rating']['average'] if 'rating' in movie.keys() else '无'




    # 如果key不存在，返回空
    def set_key(self,key,movie):
        if type(movie[key]) == 'list':
            return movie[key][0] if len(movie[key]) ==1 else '/'.join(movie[key])
        if type(movie[key]) == 'dict':
            return
        return movie['key'] if key in movie.keys() else ''





if __name__ == "__main__":
    movie_spider = Movie_spider('in_theaters')
    movie_view_model = MovieViewModel_2(movie_spider.movies[0])
    print(movie_view_model.__dict__)
