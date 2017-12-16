# coding=utf-8


from settings import useragents,filtered_name_dir,baike_dir,baike_without_html_dir
from lxml import etree
from random import choice
from bs4 import BeautifulSoup

import requests,re

pattern = re.compile(r'共(.*?)个义项')
pattern_now = re.compile(r'label-module="para"><a target=_blank href="(.*?)" data-lemmaid')
pattern_now2 = re.compile(r'label-module="para"><a target="_blank" href="(.*?)" data-lemmaid')
pattern_extract = re.compile(r'<[^>]+>')

def extract_page_content(html):
    b = BeautifulSoup(html)
    dd = pattern_extract.sub('', str(b.body.find(class_='body-wrapper')))
    return dd.replace('\n', '')

def get_page_from_baike(name):
    """
    爬取
    :param name:
    :return:
    """
    # 0.初始页抓取
    url = r'https://baike.baidu.com/item/' + name
    # print r'https://baike.baidu.com/item/' + name
    headers = {'User-Agent': choice(useragents)}
    resp = requests.get(url, verify=False, headers=headers)

    # 1.重置初始页
    if('class="lemmaWgt-subLemmaListTitle"' in resp.content):
        match_now = pattern_now.findall(resp.content)
        if(len(match_now) != 0):
            resp = requests.get(r'https://baike.baidu.com' + match_now[0], verify=False, headers=headers)
        else:
            match_now = pattern_now2.findall(resp.content)
            resp = requests.get(r'https://baike.baidu.com' + match_now[0], verify=False, headers=headers)

    # 2.从初始页开始爬取
    page_contents = []
    if ('多义词' in resp.content or '选择浏览' in resp.content):
        print name, '是多义词'
        page_contents.append(extract_page_content(resp.content))
        match = pattern.search(resp.content)
        if match:
            try:
                num = int(match.group(1))
            except Exception:
                print name, '页面中的多义词项抽取失败'
        tree = etree.HTML(resp.content)
        for i in range(1, num):
            link = tree.xpath(r"/html/body/div[3]/div[1]/div/ul/li[" + str(i + 1) + r"]/a/@href")
            # print r"/html/body/div[3]/div[1]/div/ul/li[" + str(i + 1) + r"]/a"
            # print link[0]
            if (len(link) != 0):
                content = requests.get(u'https://baike.baidu.com' + link[0], verify=False, headers=headers).content
                page_contents.append(extract_page_content(content))
    elif('百度百科错误页' in resp.content and '您所访问的页面不存在...' in resp.content and '秒后自动跳转到' in resp.content):
        print name, '百科中没有收录'
    else:
        print name, '不是多义词'
        page_contents.append(extract_page_content(resp.content))
    return page_contents

if __name__ == '__main__':
    # 百科抓取
    # content = []
    # with open(filtered_name_dir) as f:
    #     output_file = open(baike_dir, 'a')
    #     for index,line in enumerate(f):
    #         baike_now = get_page_from_baike(line.split(',')[0])
    #         output_file.write(line.split(',')[0] + ',' + str(baike_now).replace(',','').replace('\n','') + '\n')
    #         output_file.flush()
    #     output_file.close()

    # 合并
    # f1 = open(u'C:\\Users\LuckyGong\Documents\Github\cs_knowledge_graph\data\百科1.csv')
    # f2 = open(u'C:\\Users\LuckyGong\Documents\Github\cs_knowledge_graph\data\百科2.csv')
    # f = open(u'C:\\Users\LuckyGong\Documents\Github\cs_knowledge_graph\data\百科.csv','w')
    # for line in f1:
    #     f.write(line)
    # f1.close()
    # for line in f2:
    #     f.write(line)
    # f2.close()
    # f.close()

    # 去除人名
    # in_f = open(u'C:\\Users\LuckyGong\Documents\Github\cs_knowledge_graph\data\百科.csv')
    # out_f = open(u'C:\\Users\LuckyGong\Documents\Github\cs_knowledge_graph\data\百科（无名字）.csv','w')
    # for line in in_f:
    #     line_new = line[line.find(',') + 1:]
    #     out_f.write(line_new)
    # in_f.close()
    # out_f.close()

    pass