# _*_ coding: utf-8 _*_
from enum import Enum

__author__ = 'john'


class In_theaters_status(Enum):
    in_theaters = 'in_theaters'
    coming_soon = 'coming_soon'
    un_theaters = 'un_theaters'

class Match_status(Enum):
    # 待匹配
    wait_match = 1
    # 取消匹配
    cancel_match = 2
    # 匹配过期
    match_overdue = 3
    # 匹配成功
    match_success = 4

    @classmethod
    def match_status_str(cls, status):
        key_map = {
            cls.wait_match: '待合影',
            cls.cancel_match: '已取消',
            cls.match_overdue: '已失效',
            cls.match_success: '已合影'
        }
        return key_map[status]

class Movie_subjoin_status(Enum):
    # 正在上映
    in_theaters = 1
    # 即将上映
    coming_soon = 2



class Group_status(Enum):
    # 已组队待合影
    wait_watch = 1
    # 组队已取消
    cancel_watch = 2
    # 已观影
    has_been_watch = 3


    @classmethod
    def group_status_str(cls, status):
        key_map = {
            cls.wait_watch: '待观影',
            cls.cancel_watch: '已取消',
            cls.has_been_watch: '已观影'
        }
        return key_map[status]