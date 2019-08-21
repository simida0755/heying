# _*_ coding: utf-8 _*_
import datetime
import time

__author__ = 'john'


a = datetime.date.today()
print(a.strftime("%Y-%m-%d"))


# 2.把字符串转成datetime
def string_toDatetime(st):
    return datetime.datetime.strptime(st, "%Y-%m-%d")


# 3.把字符串转成时间戳形式
def string_toTimestamp(st):
    return time.mktime(time.strptime(st, "%Y-%m-%d %H:%M:%S"))

# 5.把datetime类型转外时间戳形式
def datetime_toTimestamp(dt):
    print("5.把datetime类型转外时间戳形式:", time.mktime(dt.timetuple()))

def compare_time(str):

    result =  string_toDatetime(str) >= datetime.datetime.today()
    return result if result else False

print(compare_time('2019-07-26'))