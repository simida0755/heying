# _*_ coding: utf-8 _*_
__author__ = 'john'

str = '545645sdasdf(我)11'
number = filter(lambda x: x if x.isdigit() else '',list(str))

print(int(''.join(number)))