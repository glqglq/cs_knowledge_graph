# coding=utf-8

import re,json,jieba

from settings import baike_dir,corpus_data_dir

regex = re.compile(r'\\(?![/u"])')
out_f = open(u'C:\\Users\LuckyGong\Documents\Github\cs_knowledge_graph\data\语料库\语料库（百科）.txt','w')



with open(baike_dir) as baike:
    for line in baike:
        now = line[line.find(',') + 1:]

        print unicode(line)
        sentence_seged = jieba.cut(line.strip())
        outstr = ''
        for word in sentence_seged:
            # print word,
            if word:
                if word != '\t':
                    outstr += word
                    outstr += " "
        out_f.write((outstr + '\r\n').encode('utf-8'))
#         str = line.strip().replace('(', '[').replace(')', ']').replace('\'', '"').replace('" "', '","').replace('\' \'', '","')
#         str = regex.sub(r"\\\\", str)
#         print str
#         try:
#             list2 = json.loads(str[str.index(',') + 1:])
#         except:
#             list2 = []
#         for peo in list2:
#             out_f.write(peo)