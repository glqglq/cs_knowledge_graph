# coding=utf-8
from gensim.models import word2vec

from settings import corpus_data_dir,model_dir,baike_without_html_dir,filtered_name_dir,cs_baike_dict,res_dir,baike_dir

import jieba,json,re

regex = re.compile(r'\\(?![/u"])')

def train():
    sentences = word2vec.Text8Corpus(corpus_data_dir)  # 加载语料
    model = word2vec.Word2Vec(sentences, sg = 1,window = 10)  # 默认window=5
    model.save(model_dir)
    return model

if __name__ == '__main__':
    model = train()
    out_f = open(res_dir,'a')
    with open(filtered_name_dir) as names:
        with open(baike_without_html_dir) as baikes:
            while(True):
                try:
                    now_name = names.next()
                    now_baike = baikes.next()
                    list1 = list(jieba.cut(now_name.split(',')[1]))
                    str = now_baike.replace('(', '[').replace(')', ']').replace('\'', '"').replace('" "', '","')
                    # print '0.',list(jieba.cut(now_name.split(',')[1]))
                    # print '1.',str[str.index(',') + 1:]
                    str = regex.sub(r"\\\\", str)
                    # print '2.',str[str.index(',') + 1:]
                    try:
                        list2 = json.loads(str[str.index(',') + 1:])
                    except:
                        print now_name.split(',')[0],'解码错误'
                        list2 = ['']
                    # print '3.',list2
                    if(list2 == []):
                        list2 = ['']
                    # print '4.',list(jieba.cut(list2[0]))
                    max_peo = 0
                    res_peo = ''
                    for peo in list2:
                        if(peo is ''):
                            break
                        now_peo = model.n_similarity(list1 + cs_baike_dict, list(jieba.cut(peo)))
                        if max_peo < now_peo:
                            max_peo = now_peo
                            res_peo = peo
                    out_f.write(res_peo)
                    out_f.flush()
                except StopIteration:
                    break