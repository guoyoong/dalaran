# coding=utf-8

import time


class TimeUtil:

    def __init__(self):
        print "init"

    @staticmethod
    def format_date(date_source):
        try:
            timestamp = time.mktime(time.strptime(date_source, '%Y-%m-%d'))
            return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(timestamp))
        except:
            return ""
