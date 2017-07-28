# coding=utf-8

from mongoengine import *


class YuqingSpiderMonitor(Document):
    _id = StringField(default='')
    key = StringField(default='')
    crawl_pages = StringField(default='')
    new_pages = StringField(default='')
    source_type = StringField(default='')
    duration = StringField(default='')
    date_stat = StringField(default='')


class YuqingSourceItem(Document):
    _id = StringField(default='')
    source_name = StringField(default='')
    source_short = StringField(default='')
    source_type = StringField(default='')
    key_word = StringField(default='')
    source_url = StringField(default='')

