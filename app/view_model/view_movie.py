# _*_ coding: utf-8 _*_
__author__ = 'john'


# _*_ coding: utf-8 _*_
__author__ = 'john'

class MovieViewModel:

    def __init__(self,movie,keyword):
        self.mid = movie['id']
        self.title = movie['title']
        print(self.title)
        self.images = movie['images']['large'] if movie['images']['small'] else ''
        self.directors = '/'.join([directors['name'] for directors in movie['directors']])
        self.genres = '/'.join(movie['genres'])if 'genres' in movie.keys() else ''
        self.casts = '/'.join([casts['name'] for casts in movie['casts']]) or ''
        self.durations = movie['durations'][0] if 'durations' in movie.keys() and movie['durations'] else ''
        self.pubdates = '/'.join(movie['pubdates'])
        self.mainland_pubdate = self.mainland_pubdate_init(movie)
        self.average = movie['rating']['average'] if 'rating' in movie.keys() else ''
        self.keyword = keyword



    def mainland_pubdate_init(self,movie):
        if movie['mainland_pubdate']:
            return movie['mainland_pubdate']
        elif '中国大陆' in self.pubdates:
            return self.process_str(self.pubdates)
        elif len(self.pubdates) == 10:
            return self.pubdates
        else:
            return ''


    @classmethod
    def process_str(cls,str):
        to_str = str.split('(中国')[0].split('/')
        return to_str[len(to_str)-1]

    @staticmethod
    def list_to_str(list):
        if len(list) == 1:
            return list[0]
        return '/'.join(list)

class MovieViewCollection:
    def __init__(self):
        self.total = 0
        self.movies = []
        self.keyword = ''

    def fill(self,movie_spider):
        self.total = self.total + int(movie_spider.total)
        self.movies = self.movies + [MovieViewModel(movie,movie_spider.in_theaters_status) for movie in movie_spider.movies]