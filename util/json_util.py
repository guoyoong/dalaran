# coding=utf-8

import sys
from bson import json_util
reload(sys)
sys.setdefaultencoding('utf-8')


class JsonGenUtil:

    def __init__(self):
        print 'init'

    @staticmethod
    def generate_ok(msg):
        return json_util.dumps({"status": "1", "msg": msg})

    @staticmethod
    def generate_error(msg):
        return json_util.dumps({"status": "-1", "msg": msg})

