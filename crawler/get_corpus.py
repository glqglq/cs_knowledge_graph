# coding=utf-8
import re,requests

from random import choice
from settings import useragents
from url_cleaning import all_url_cleaning
from jparser import PageModel

link_pattern = re.compile(r'href=\".*?\"', re.M)
urls = set([u'http://www.ccf.org.cn'])
finished_urls = set([])
def get_corpus_from_web(file,href):
    print href
    if('ccf.org' not in href):
        return
    headers = {'User-Agent': choice(useragents)}
    resp = requests.get(href, verify=False, headers=headers)
    new_urls = link_pattern.findall(resp.content)
    result_body = PageModel(resp.content.decode('utf-8')).extract()
    result_body_temp = ''
    for x in result_body['content']:
        if x['type'] == 'text':
            result_body_temp += x['data'].replace(' ','').replace('\n','')
    # print result_body_temp
    file.write(result_body_temp)
    finished_urls.add(href)
    for url in all_url_cleaning(resp.url,new_urls):
        # print url,
        if url not in finished_urls:
            urls.add(url)

if __name__ == '__main__':
    f = open(u'C:\\Users\LuckyGong\Documents\Github\cs_knowledge_graph\data\语料库.txt','a')

    while urls:
        try:
            url = urls.pop()
            get_corpus_from_web(f,url)
        except:
            print url,'页面错误'