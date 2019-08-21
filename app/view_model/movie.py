# _*_ coding: utf-8 _*_
__author__ = 'john'

class MovieViewModel:

    def __init__(self,movie):
        self.mid = movie['id']
        self.title = movie['title']
        print(self.title)
        self.images = movie['images']['large'] if movie['images']['small'] else ''
        self.directors = '/'.join([directors['name'] for directors in movie['directors']])
        self.genres = '/'.join(movie['genres'])if 'genres' in movie.keys() else '未知'
        self.casts = '/'.join([casts['name'] for casts in movie['casts']]) or ''
        self.durations = movie['durations'][0] if 'durations' in movie.keys() and movie['durations'] else '未知'
        self._mainland_pubdate = movie['mainland_pubdate']
        self.pubdates = '/'.join(movie['pubdates'])
        self.average = movie['rating']['average'] if 'rating' in movie.keys() else '无'


    @property
    def mainland_pubdate(self):
        if self._mainland_pubdate:
            return self._mainland_pubdate
        elif '中国大陆' in self.pubdates:
            return self.process_str(self.pubdates)
        elif len(self.pubdates) == 10:
            return self.pubdates
        else:
            return '大陆暂无'

    # def do_mainland_pubdate(self):
    #     if self._mainland_pubdate:
    #         self.mainland_pubdate =  self._mainland_pubdate
    #     elif '中国大陆' in self.pubdates:
    #         self.mainland_pubdate = self.process_str(self.pubdates)
    #     elif len(self.pubdates) == 10:
    #         self.mainland_pubdate = self.pubdates
    #     else:
    #         self.mainland_pubdate = '大陆暂无'

    @classmethod
    def process_str(cls,str):
        to_str = str.split('(中国')[0].split('/')
        return to_str[len(to_str)-1]

    @staticmethod
    def list_to_str(list):
        if len(list) == 1:
            return list[0]
        return '/'.join(list)

class MovieCollection:
    def __init__(self):
        self.total = 0
        self.movies = []
        self.keyword = ''

    def fill(self,movie_spider):
        self.total = movie_spider.total
        self.keyword = movie_spider.in_theaters_status
        self.movies = [MovieViewModel(movie) for movie in movie_spider.movies]