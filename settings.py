# -*- coding:utf-8 -*-
ccf_tc_base_url = r'http://www.ccf.org.cn/tc/zwmd/'  #ccf专委会基地址
ccd_tc = ["dmtjstc","fwjs","gxnjs","gykzjsj","hlw","jsjaq","jsjfzsjytxx","jsjgcygy","jsjsj","jsjyy","jy","fbsjsycl","kelhjjsj","lljsjkx","psjs","qrsxt","rgznymssb","rjjh","rcjs","rjgc","sjk","txjg","wlysjtx","wlw","xtrj","xtjs","xxbm","xxccjs","xxxt","xnxsykshjs","zwxxjs","dsjzjwyh","swxxxzyz","xshffzyz"] #ccf专委会子地址
# ccd_tc = ["rgznymssb"]
useragents = [
    "Avant Browser/1.2.789rel1 (http://www.avantbrowser.com)",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.5 (KHTML, like Gecko) Chrome/4.0.249.0 Safari/532.5",
    "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.310.0 Safari/532.9",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/9.0.601.0 Safari/534.14",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/10.0.601.0 Safari/534.14",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.20 (KHTML, like Gecko) Chrome/11.0.672.2 Safari/534.20",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.27 (KHTML, like Gecko) Chrome/12.0.712.0 Safari/534.27",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.24 Safari/535.1",
    "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0 x64; en-US; rv:1.9pre) Gecko/2008072421 Minefield/3.0.2pre",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.10) Gecko/2009042316 Firefox/3.0.10",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-GB; rv:1.9.0.11) Gecko/2009060215 Firefox/3.0.11 (.NET CLR 3.5.30729)",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 GTB5",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; tr; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 ( .NET CLR 3.5.30729; .NET4.0E)",
    "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
    "Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0a2) Gecko/20110622 Firefox/6.0a2",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:7.0.1) Gecko/20100101 Firefox/7.0.1",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:2.0b4pre) Gecko/20100815 Minefield/4.0b4pre",
    "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.0 )",
    "Mozilla/4.0 (compatible; MSIE 5.5; Windows 98; Win 9x 4.90)",
    "Mozilla/5.0 (Windows; U; Windows XP) Gecko MultiZilla/1.6.1.0a",
    "Mozilla/2.02E (Win95; U)",
    "Mozilla/3.01Gold (Win95; I)",
    "Mozilla/4.8 [en] (Windows NT 5.1; U)",
    "Mozilla/5.0 (Windows; U; Win98; en-US; rv:1.4) Gecko Netscape/7.1 (ax)",
]

TOP_LEVEL_DOMAINS = [r'.com',r'.cn',r'.co',r'.edu',r'.gov',r'.net',r'.cc',r'.me',r'.org',r'.gov',r'.cc',r'.hk',r'.tv']

mongodb_ip = 'localhost'
mongodb_port = 27017

cs_baike_dict_temp = {'教授':1,'计算机':1,'讲师':1,'研究员':1,'ccf':1,'CCF':1,'IEEE':1,'云计算':1,'信息':1,'院士':1,'大学':1,'研究所':1}
cs_baike_dict = ['教授','计算机','讲师','研究员','ccf','CCF','IEEE','云计算','大数据','信息','院士','大学','研究所']

name_file_dir = u'C:\\Users\LuckyGong\Documents\GitHub\cs_knowledge_graph\data\ccf专家数据\专家名（有location）.csv'
filtered_name_dir = u'C:\\Users\LuckyGong\Documents\Github\cs_knowledge_graph\data\ccf专家数据\专家名（初步去重后）2.csv'
baike_dir = u'C:\\Users\LuckyGong\Documents\Github\cs_knowledge_graph\data\百科数据\百科.csv'
baike_without_html_dir = u'C:\\Users\LuckyGong\Documents\Github\cs_knowledge_graph\data\百科数据\百科.csv'
stop_word_dir = u'C:\\Users\LuckyGong\Documents\Github\cs_knowledge_graph\data\停用词.txt'
corpus_data_dir = u'C:\\Users\LuckyGong\Documents\Github\cs_knowledge_graph\data\语料库\语料库（去除英文停词分词）.txt'
model_dir = u'C:\\Users\LuckyGong\Documents\Github\cs_knowledge_graph\model.model'
res_dir = ur'C:\\Users\LuckyGong\Documents\Github\cs_knowledge_graph\data\result.txt'