# -*- coding: utf-8 -*-

# import urllib2
#
# data = open('./all_buy.txt', 'rb').read()
# req = urllib2.Request('http://10.100.124.226:9200/test/test/_bulk', data)
# req.add_header('Content-Length', '%d' % len(data))
# req.add_header('Content-Type', 'application/octet-stream')
# res = urllib2.urlopen(req)


# selenium

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")

# 添加Cookie
driver.add_cookie({'name': 'BAIDUID', 'value': 'AAAAAAAAAAAAAAA:FG=1'})
driver.add_cookie({'name': 'BDUSS', 'value': 'AAAAAAAAAAAAAAAAAAAA'})

# 刷新页面
driver.refresh()


