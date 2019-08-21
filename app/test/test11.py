# _*_ coding: utf-8 _*_
__author__ = 'john'


def process_str(str):
    return str.split('(中国')[0][-10:]

print(type(process_str("2015-05-19(中国电影节)/2015-06-17()")))