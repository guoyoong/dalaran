# coding=utf-8

from mongo_item import *
from mongo.settings import MONGODB_URI
from mongoengine import *

import sys

reload(sys)
sys.setdefaultencoding('utf-8')


class MongoClient:
    connect('yuqing', host=MONGODB_URI['host'], port=MONGODB_URI['port'],
            username=MONGODB_URI['username'], password=MONGODB_URI['password'])

    def __init__(self):
        print 123

    @staticmethod
    def get_yuqing_monitor(start_date, end_date):
        items = YuqingSpiderMonitor.objects(Q(date_stat__gte=start_date) & Q(date_stat__lte=end_date)).exclude('_id')
        out = MongoClient.encode_document(items)
        return out

    @staticmethod
    def yq_source_list():
        items = YuqingSourceItem.objects().exclude('_id')
        out = MongoClient.encode_document(items)
        return out

    @staticmethod
    def encode_document(obj):
        if isinstance(obj, QuerySet):
            result = []
            for item in obj:
                out = dict()
                for field in item:
                    if field != 'auto_id_0' and field != '_id':
                        out[field] = item[field]
                result.append(out)
            return result
