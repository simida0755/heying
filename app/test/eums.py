# _*_ coding: utf-8 _*_
from enum import Enum

__author__ = 'john'


class Match_status2(Enum):
    # 待匹配
    wait_match = 1
    # 取消匹配
    cancel_match = 2
    # 匹配过期
    match_overdue = 3
    # 匹配成功
    match_success = 4

print(Match_status2.wait_match.value)
print(Match_status2(1).value)