# coding: utf-8

import json

import jieba.analyse
import matplotlib as mpl
from PIL import Image
from wordcloud import WordCloud
import numpy as np

# mpl.use('TkAgg')
import matplotlib.pyplot as plt


def keywords(mblogs):
    text = []
    for blog in mblogs:
        keyword = jieba.analyse.extract_tags(blog['text'])
        text.extend(keyword)
    return text


def gen_img(texts, img_file):
    data = ' '.join(text for text in texts)
    image_coloring = Image.open(img_file)
    image_coloring = np.asanyarray(image_coloring)
    wc = WordCloud(
        background_color='white',
        mask=image_coloring,
        font_path='C:/Users/wy_yx/Desktop/weibo_wordcloud-master/FZXBSJW.TTF'
    )
    wc.generate(data)

    # plt.figure()
    # plt.imshow(wc, interpolation="bilinear")
    # plt.axis("off")
    # plt.show()

    wc.to_file(img_file.split('.')[0] + '_wc.png')


if __name__ == '__main__':
    keyword = '冠状病毒'
    mblogs = json.loads(open('result_{}.json'.format(keyword), 'r', encoding='utf-8').read())

    words = []
    for blog in mblogs:
        words.extend(jieba.analyse.extract_tags(blog['text']))

    delete_word = ["全文", "微博", "视频", "链接"]
    for i in delete_word:
        while i in words:
            words.remove(i)
    gen_img(words, '冠状病毒.png')
    keyword = '武汉'
    mblogs = json.loads(open('result_{}.json'.format(keyword), 'r', encoding='utf-8').read())
    for i in delete_word:
        while i in words:
            words.remove(i)
    words = []
    for blog in mblogs:
        words.extend(jieba.analyse.extract_tags(blog['text']))

    for i in delete_word:
        while i in words:
            words.remove(i)
    gen_img(words, '武汉.png')
    keyword = '口罩'
    mblogs = json.loads(open('result_{}.json'.format(keyword), 'r', encoding='utf-8').read())
    for i in delete_word:
        while i in words:
            words.remove(i)
    words = []
    for blog in mblogs:
        words.extend(jieba.analyse.extract_tags(blog['text']))

    for i in delete_word:
        while i in words:
            words.remove(i)
    gen_img(words, '口罩.png')
    keyword = '肺炎'
    mblogs = json.loads(open('result_{}.json'.format(keyword), 'r', encoding='utf-8').read())
    words = []
    for blog in mblogs:
        words.extend(jieba.analyse.extract_tags(blog['text']))
    for i in delete_word:
        while i in words:
            words.remove(i)
    gen_img(words, '肺炎.png')