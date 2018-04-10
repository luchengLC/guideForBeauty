#!/usr/bin/python
# -*- coding:utf-8 -*-

import os
import jieba
import jieba.analyse
import re
from gensim.models import word2vec
from stanfordcorenlp import StanfordCoreNLP
from gensim import corpora, models, similarities

#根据topK words 找出跟这些词最接近的词汇
def get_similar_type(file_path,keywords):
    tables = ['眼','唇','香水','底妆']
    sentences=word2vec.Text8Corpus(file_path+"solved_comments/cut_stop_words.txt")
    model=word2vec.Word2Vec(sentences, size=100)
    print(keywords)
    max = 0
    type = ''
    for i in tables:
        print(i)
        words = []
        words.append(keywords)
        for j in model.most_similar(keywords):
            words.append(j[0])
        # fout.write(','.join(words) + '\n')
        similarity = model.similarity(i,keywords)
        if similarity>max:
            type = i
        print(words)

    print(type,max)

    if type=='眼妆':
        return ['product_eye']
    elif type=='唇妆':
        return ['product_lipstick']
    elif type=='香水':
        return ['product_perfume', 'product_other_perfume']
    else:
        return ['product_baseMakeup']


if __name__ == '__main__':
    file_path = (os.path.dirname(os.path.dirname(os.path.abspath("similarity_util.py"))) + '/data/').replace('\\','/')
    keyword = '卡姿兰'
    # keyword = '卡姿兰气垫'
    get_similar_type(file_path, keyword)


