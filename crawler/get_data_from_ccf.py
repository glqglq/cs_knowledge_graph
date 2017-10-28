# -*- coding: utf-8 -*-
import requests,re,sys,pymongo
from settings import ccf_tc_base_url,ccd_tc,useragents,mongodb_ip,mongodb_port,name_file_dir
from random import choice


reload(sys)
sys.setdefaultencoding('utf-8')


def get_name_from_ccf_tc():
    """

    :return:
    """
    people = []
    pa1 = re.compile(r'style="cursor: default;">(.+)</a>')
    pa2 = re.compile(r'<li>\s*?<span>(.*?)</span>')
    for suffix in ccd_tc:
        content = requests.get(ccf_tc_base_url + suffix).content
        people.extend(pa1.findall(content))
        people.extend(pa2.findall(content))

    for i in range(len(people)):
        people[i] = people[i].replace('　','')

    print len(people)
    for peo in people:
        print peo

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
    if('target="_blank">多义词</a>' in resp.content):
        print name,'是多义词'
        collection.insert({'name':name,'page_content':resp.content})
    else:
        print name,'不是多义词'

if __name__ == '__main__':
    # get_name_from_ccf_tc()
    conn = pymongo.MongoClient(mongodb_ip, mongodb_port)
    db = conn.admin
    collection = db.baike

    with open(name_file_dir,'r') as f:
        for name in f:
            get_page_from_baike(collection,name.strip())