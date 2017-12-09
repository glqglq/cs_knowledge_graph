# -*- coding: utf-8 -*-
import requests,re,sys
from settings import ccf_tc_base_url,ccd_tc,name_file_dir

from bs4 import BeautifulSoup

reload(sys)
sys.setdefaultencoding('utf-8')

def get_name_from_ccf_tc():
    people = []
    for suffix in ccd_tc:
        # 0.页面抓取
        content = requests.get(ccf_tc_base_url + suffix).content

        # 1.主任、秘书长、副主任
        res = re.findall(r'>([\d]|[\D]*)</a></h3>\s+<p>([\d]|[\D]*)</p>\s+<p>([\d]|[\D]*)</p>',content.replace(r'\n',r''),re.S)
        for i in res:
            now = {}
            now['name'] = i[0]
            now['location'] = i[1]
            now['email'] = i[2]
            people.append(now)

        # 2.荣誉委员、常务委员、委员
        soup = BeautifulSoup(content, "lxml")
        tag = soup.find_all('ul', attrs={'class': 'g-ul m-list3'})
        for i in tag:
            for child in i.children:
                # 一个人
                now = {}
                now_index = 0
                for c in child:
                    # 一个人的不同属性
                    for n in c:
                        try:
                            if n.strip() != '':
                                if(now_index == 0):
                                    now['name'] = n
                                elif(now_index == 1):
                                    now['location'] = n
                                elif(now_index == 2):
                                    now_index = 0
                                    now['email'] = n
                                    break
                                now_index += 1
                        except:
                            print '出错！！'
                people.append(now)
    for p in people:
        if p.has_key('name'):
            print p['name'].replace(' ','').replace('　','').replace('\n','').replace('\t',''),
            if p.has_key('location'):
                print p['location'].replace(' ','').replace('　','').replace('\n','').replace('\t',''),
            if p.has_key('email'):
                print p['email'].replace(' ', '').replace('　', '').replace('\n', '').replace('\t', ''),
        print