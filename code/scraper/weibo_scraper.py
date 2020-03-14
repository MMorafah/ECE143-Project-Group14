# coding: utf-8

import re
import json
import requests

url_template = "https://m.weibo.cn/api/container/getIndex?type=wb&queryVal={}&containerid=100103type=2%26q%3D{}&page={}"


def clean_text(text):
    '''
    test: input str
    '''
    assert isinstance(text,str)
    dr = re.compile(r'(<)[^>]+>', re.S)
    dd = dr.sub('', text)
    dr = re.compile(r'#[^#]+#', re.S)
    dd = dr.sub('', dd)
    dr = re.compile(r'@[^ ]+ ', re.S)
    dd = dr.sub('', dd)
    return dd.strip()


def fetch_data(query_val, page_id):
    '''
    query_val:keywords
    page_id:page id
    '''
    assert isinstance(query_val,str)
    assert isinstance(page_id,int)
    assert page_id>0
    resp = requests.get(url_template.format(query_val, query_val, page_id))
    card_group = json.loads(resp.text)['data']['cards'][0]['card_group']

    mblogs = []
    for card in card_group:
        mblog = card['mblog']
        blog = {'mid': mblog['id'],
                'text': clean_text(mblog['text']),
                'userid': str(mblog['user']['id']),
                'username': mblog['user']['screen_name'],
                'reposts_count': mblog['reposts_count'],
                'comments_count': mblog['comments_count'],
                'attitudes_count': mblog['attitudes_count']
                }
        mblogs.append(blog)
    return mblogs


def remove_duplication(mblogs):
    '''
    remove duplication by 'mid'
    mblogs:list of dict
    '''
    assert isinstance(mblogs,list)
    mid_set = {mblogs[0]['mid']}
    new_blogs = []
    for blog in mblogs[1:]:
        if blog['mid'] not in mid_set:
            new_blogs.append(blog)
            mid_set.add(blog['mid'])
    return new_blogs


def fetch_pages(query_val, page_num):
    '''
    query_val:keywords
    page_num:total fetch page number
    '''
    assert isinstance(query_val,str)
    assert isinstance(page_num,int)
    assert page_num>0
    mblogs = []
    for page_id in range(1 + page_num + 1):
        try:
            mblogs.extend(fetch_data(query_val, page_id))
        except Exception as e:
            print(e)


    mblogs = remove_duplication(mblogs)#remove duplication
    #translate
    if query_val=='冠状病毒':
        query_val ='COVID-19'
    if query_val=='武汉':
        query_val ='wuhan'
    if query_val=='肺炎':
        query_val ='pneumonia'
    if query_val=='口罩':
        query_val ='face-mask'
    fp = open('../../data/Weibo/result_{}.json'.format(query_val), 'w', encoding='utf-8')#open file
    json.dump(mblogs, fp, ensure_ascii=False, indent=4)#save result


if __name__ == '__main__':
    fetch_pages('冠状病毒', 50)
    fetch_pages('武汉', 50)
    fetch_pages('肺炎', 50)
    fetch_pages('口罩', 50)
