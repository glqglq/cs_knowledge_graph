# -*- coding: utf-8 -*-
import requests,re,sys
from settings import ccf_tc_base_url,ccd_tc,name_file_dir

from bs4 import BeautifulSoup

reload(sys)
sys.setdefaultencoding('utf-8')

def get_name_from_ccf_tc():
    """
    抓取ccf专委人物信息
    :return:
    """
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

def process_data_from_ccf(path):
    """
    ccf专委名单去重
    :param path:专委名单路径
    :return:
    """
    peo = []
    res_peo = []
    with open(path) as f:
        for line in f:
            peo.append([line.split(r',')[0],line.split(r',')[1],line.split(r',')[2]])

        for i in range(len(peo)):
            flag = False
            for j in range(len(res_peo) - 1,-1,-1):
                if(peo[i][0] == res_peo[j][0] and peo[i][1] in res_peo[j][1]):
                    flag = True
                    break
                elif(peo[i][0] == res_peo[j][0] and res_peo[j][1] in peo[i][1]):
                    flag = True
                    res_peo[j][1] = peo[i][1]
                    break
                elif(peo[i][0] == res_peo[j][0] and res_peo[j][2] == peo[i][2]):
                    flag = True
                    break
                elif(peo[i][0] == res_peo[j][0]):
                    continue
            if(not flag):  # 未合并
                    res_peo.append(peo[i])

    for peo in res_peo:
        print peo[0],peo[1],peo[2]

if __name__ == '__main__':
    get_name_from_ccf_tc()
    process_data_from_ccf(name_file_dir)