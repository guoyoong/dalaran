# coding=utf-8

from flask import Flask
from flask import request
from mongo.mongo_client import *
from util.time_util import *
from util.md5_util import *
from util.json_util import *
from bson import json_util
app = Flask(__name__)

reload(sys)
sys.setdefaultencoding('utf-8')


@app.route('/dalaran/yqmonitor')
def yqmonitor():
    start_date = request.args.get('start_date', '')
    end_date = request.args.get('end_date', '')
    result = dict()
    start_date = TimeUtil.format_date(start_date)
    end_date = TimeUtil.format_date(end_date)
    if start_date == '' or end_date == '':
        return ""

    result['data'] = MongoClient.get_yuqing_monitor(start_date, end_date)
    return json_util.dumps(result)


@app.route('/dalaran/yq_source_list')
def yq_source_list():
    result = dict()
    result['data'] = MongoClient.yq_source_list()
    return json_util.dumps(result, separators=(',', ':')).encode('utf-8')


@app.route('/dalaran/yq_source_save')
def yq_source_save():
    try:
        yqitem = YuqingSourceItem()
        yqitem.source_name = request.args.get('source_name', '')
        yqitem.source_type = request.args.get('source_type', '')
        yqitem.source_short = request.args.get('source_short', '')
        yqitem._id = Md5Util.generate_md5(yqitem.source_short)
        yqitem.source_url = request.args.get('source_url', '')
        yqitem.key_word = request.args.get('key_word', '')
        if(yqitem.source_name == '' or yqitem.source_type == '' or yqitem.source_short == ''
           or yqitem.source_url == '' or yqitem.key_word == ''):
            return JsonGenUtil.generate_error("信息不完整")
        yqitem.save()
        return JsonGenUtil.generate_ok("")
    except:
        return JsonGenUtil.generate_error("保存失败")


@app.route('/dalaran/test')
def test():
    return "test"


if __name__ == '__main__':
    app.debug = True
    app.run(host='10.100.157.197', port=5000, threaded=True)
