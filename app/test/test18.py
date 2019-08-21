# _*_ coding: utf-8 _*_
__author__ = 'john'

movie_keyword = {
    'set_movie':{'in_theaters':'in_theaters',
                 'coming_soon':'coming_soon'}

}
movie = {
    'a':'1',
    'b':'2'
}
for key,value in movie.items():
    print(key,value)

for a in movie.values():
    print(a)