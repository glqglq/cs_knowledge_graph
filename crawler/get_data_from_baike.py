# coding=utf-8

from random import choice
from settings import useragents

import requests

def get_page_from_baike(collection,name):
    """
    爬取
    :param name:
    :return:
    """

    url = u'https://baike.baidu.com/item/' + name
    headers = {'User-Agent':choice(useragents)}
    resp = requests.get(url,verify = False,headers = headers)
    # print resp.content
    if('多义词' in resp.content or '选择浏览' in resp.content):
        print name,'是多义词'
    elif('您所访问的页面不存在' in resp.content):
        print name,'百科中没有收录'

    else:
        print name,'不是多义词'
        collection.insert({'name': name, 'page_content': resp.content})