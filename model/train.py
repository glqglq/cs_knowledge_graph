# coding=utf-8
from gensim.models import word2vec

from settings import corpus_data_dir,model_dir,baike_without_html_dir,filtered_name_dir

import jieba,json

def train():
    sentences = word2vec.Text8Corpus(corpus_data_dir)  # 加载语料
    model = word2vec.Word2Vec(sentences, size=200)  # 默认window=5
    model.save(model_dir)
    return model

if __name__ == '__main__':
    model = train()

    with open(filtered_name_dir) as names:
        with open(baike_without_html_dir) as baikes:
            while(True):
                try:
                    now_name = names.next()
                    now_baike = baikes.next()
                    list1 = list(jieba.cut(now_name.split(',')[1]))
                    str = str.replace('(', '[').replace(')', ']').replace('\'', '"').replace('" "', '","')
                    list2 = json.loads(str[str.index(',') + 1:])
                    max_peo = 0
                    res_peo = ''
                    for peo in list2:
                        now_peo = model.n_similarity(list1, list(jieba.cut(peo)))
                        if max_peo < now_peo:
                            max_peo = now_peo
                            res_peo = peo
                            # TODO 写入文件
                except StopIteration:
                    break