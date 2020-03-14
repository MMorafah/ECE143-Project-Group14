# coding: utf-8

import json

import jieba.analyse
import matplotlib as mpl
from PIL import Image
from wordcloud import WordCloud
import numpy as np

# mpl.use('TkAgg')
import matplotlib.pyplot as plt



def gen_img(texts, img_file,name):
    '''
    text:input string list
    img_file:input photo address
    name: file name to save word cloud
    '''
    assert isinstance(texts,list)
    assert isinstance(img_file,str)
    assert isinstance(name,str)
    data = ' '.join(text for text in texts)
    image_coloring = Image.open(img_file)
    image_coloring = np.asanyarray(image_coloring)
    wc = WordCloud(
        background_color='white',
        mask=image_coloring,
        font_path='../../data/Weibo/FZXBSJW.TTF'
    )
    wc.generate(data)

    plt.figure()
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    plt.show()

    wc.to_file('../../data/Weibo'+name + '_wc.png')


def main():
    # for COVID-19
    keyword = '冠状病毒'
    if keyword=='冠状病毒':
        keyword ='COVID-19'
    mblogs = json.loads(open('../../data/Weibo/result_{}.json'.format(keyword), 'r', encoding='utf-8').read())#read data
    words = []
    for blog in mblogs:
        words.extend(jieba.analyse.extract_tags(blog['text']))
    delete_word = ["全文", "微博", "视频", "链接"]
    for i in delete_word:
        while i in words:
            words.remove(i)#clean data
    gen_img(words, '../../data/Weibo/original.png',keyword)
    
    # for wuhan
    keyword = '武汉'
    if keyword=='武汉':
        keyword ='wuhan'
    mblogs = json.loads(open('../../data/Weibo/result_{}.json'.format(keyword), 'r', encoding='utf-8').read())#read data
    for i in delete_word:
        while i in words:
            words.remove(i)
    words = []
    for blog in mblogs:
        words.extend(jieba.analyse.extract_tags(blog['text']))
    for i in delete_word:
        while i in words:
            words.remove(i)#clean data
    gen_img(words, '../../data/Weibo/original.png',keyword)
    
    # for face mask
    keyword = '口罩'
    if keyword=='口罩':
        keyword ='face-mask'
    mblogs = json.loads(open('../../data/Weibo/result_{}.json'.format(keyword), 'r', encoding='utf-8').read())#read data
    for i in delete_word:
        while i in words:
            words.remove(i)#clean data
    words = []
    for blog in mblogs:
        words.extend(jieba.analyse.extract_tags(blog['text']))
    for i in delete_word:
        while i in words:
            words.remove(i)#clean data
    gen_img(words, '../../data/Weibo/original.png',keyword)
    
    # for pneumonia
    keyword = '肺炎'
    if keyword=='肺炎':
        keyword ='pneumonia'
    mblogs = json.loads(open('../../data/Weibo/result_{}.json'.format(keyword), 'r', encoding='utf-8').read())#read data
    words = []
    for blog in mblogs:
        words.extend(jieba.analyse.extract_tags(blog['text']))
    for i in delete_word:
        while i in words:
            words.remove(i)#clean data
    gen_img(words, '../../data/Weibo/original.png',keyword)

    
if __name__ == '__main__':
    main()
