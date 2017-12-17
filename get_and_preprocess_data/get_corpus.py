# coding=utf-8
import re,requests,jieba

from random import choice
from settings import useragents,stop_word_dir
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

def stopwordslist(filepath):
    stopwords = [line.strip() for line in open(filepath, 'r')]
    return stopwords

if __name__ == '__main__':

    # f = open(u'C:\\Users\LuckyGong\Documents\Github\cs_knowledge_graph\data\语料库.txt','a')
    # 抓取
    # while urls:
    #     try:
    #         url = urls.pop()
    #         get_corpus_from_web(f,url)
    #     except:
    #         print url,'页面错误'
    # f.close()

    # 去除连续英文
    # pattern_now = re.compile(r'^[\x01-\x7f]*$')
    # f3 = open(u'C:\\Users\LuckyGong\Documents\Github\cs_knowledge_graph\data\语料库（去除英文）.txt','w')
    #
    # with open(u'C:\\Users\LuckyGong\Documents\Github\cs_knowledge_graph\data\语料库.txt') as f2:
    #     for line in f2:
    #         if(len(pattern_now.findall(line)) == 0):
    #             f3.write(line)
    #
    #     f3.close()

    # 去除停用词
    # f = open(u'C:\\Users\LuckyGong\Documents\Github\cs_knowledge_graph\data\语料库（去除英文）.txt')
    # out_f = open(u'C:\\Users\LuckyGong\Documents\Github\cs_knowledge_graph\data\语料库（去除英文停词分词）.txt', 'a')

    # 控制行数
    # f3 = open(u'C:\\Users\LuckyGong\Documents\Github\cs_knowledge_graph\data\语料库（控制每行字符数）.txt', 'a')
    # with open(u'C:\\Users\LuckyGong\Documents\Github\cs_knowledge_graph\data\语料库.txt') as f2:
    #     for line in f2:
        # try:
        #     if(len(line.decode('utf-8')) > 1000):
        #         now = 0
        #         while True:
        #             if(now >= len(line.decode('utf-8'))):
        #                 break
        #             f3.write(line.decode('utf-8')[now:min(now + 1000,len(line))] + '\r\n')
        #             now += 1000
        #     else:
        #         f3.write(line.decode('utf-8'))
        # except:
        #     print 'Wrong!'

    # 分词、去除英语部分
    stopwords = stopwordslist(u'C:\\Users\LuckyGong\Documents\Github\cs_knowledge_graph\data\停用词.txt')  # 这里加载停用词的路径
    pattern_now = re.compile(r'^[\x01-\x7f]*$')
    f3 = open(u'C:\\Users\LuckyGong\Documents\Github\cs_knowledge_graph\data\语料库（去除英文停词分词）.txt','a')
    with open(u'C:\\Users\LuckyGong\Documents\Github\cs_knowledge_graph\data\语料库（控制每行字符数）.txt') as f2:
        for line in f2:
            if(len(pattern_now.findall(line)) == 0):
                sentence_seged = jieba.cut(line.strip())
                outstr = ''
                for word in sentence_seged:
                    if word not in stopwords and word :
                        if word != '\t':
                            outstr += word
                            outstr += " "
                f3.write(outstr + '\r\n')
        f3.close()