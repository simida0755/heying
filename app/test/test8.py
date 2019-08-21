# _*_ coding: utf-8 _*_
__author__ = 'john'

a = {
    'a':1,
    'b':2,
    'c':3
}

class Test:
    def __init__(self, dict):
        self.a = dict['f'] if 'f' in dict.keys() else 'hehe'
        self.d = dict.setdefault('d', '未知')


if __name__ == '__main__':
    test = Test(a)
    print(test.a, test.d)