#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : pureoym
# @Contact : pureoym@163.com
# @TIME    : 2018/6/27 10:07
# @File    : data_processor.py
# Copyright 2017 pureoym. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ========================================================================
import codecs
import csv
import json
import os
from utils import http_utils,data_utils

API_SIZE = 100
# NEWS_API = 'http://data.mgt.chinaso365.com/datasrv/1.0/resources/01257/search?' \
#       'fields=id,secondLable,transferTime,headLine,dataContent,bigPic' \
#       '&filters=EQS_thirdLable,突发事件|EQS_secondLable,国内新闻|NES_bigPic,NULL' \
#       '&pagestart=1&fetchsize=10'
NEWS_API = 'http://data.mgt.chinaso365.com/datasrv/1.0/resources/01257/search?' \
           'fields=id,secondLable,transferTime,headLine,dataContent,bigPic' \
           '&filters=EQS_thirdLable,突发事件|EQS_secondLable,国内新闻|NES_bigPic,NULL' \
           '&pagestart=1&fetchsize=%s' % API_SIZE


def main():
    news_list = get_news_from_api()  # 通过接口获取新闻数据
    text_process(news_list)  # 处理文本，保存至本地
    # image_process(news_list)  # 保存图片至本地


def text_process(news_list):
    """
    下载新闻正文等字段，过滤正文，并储存至本地。
    存储格式：
    ID&&&时间&&&标签&&&标题&&&正文
    :return:
    """
    for news in news_list:
        doc = news[4]
        print("input="+doc)
        print("output="+data_utils.chinese_clean(doc))


def text_process_bac(news_list):
    """
    下载新闻正文等字段，过滤正文，并储存至本地。
    存储格式：
    ID&&&时间&&&标签&&&标题&&&正文
    :return:
    """
    length = len(news_list)
    filename = 'news.csv'
    out = ''
    with open(filename, "wb") as csvfile:
        csvfile.write(codecs.BOM_UTF8)
        writer = csv.writer(csvfile, dialect=("excel"))
        # writer.writerow(map(lambda x:str.encode(x),["id", "title", "doc", "img_url"]))
        for i, news in enumerate(news_list):
            nid = str(news[0])
            title = news[3]
            doc = news[4]
            img_url = news[5]
            writer.writerow(map(lambda x: str.encode(x), [nid, title, doc, img_url]))
            if i % 10 == 0:
                print('image process : ' + str(i) + '/' + str(length))


def image_process(news_list):
    """
    下载图片，并重命名图片。重命名方法：资源主键.jpg
    :return:
    """
    length = len(news_list)
    for i, news in enumerate(news_list):
        nid = news[0]
        img_url = news[5]
        if img_url is not None:  # 如果有图片，则下载保存至本地
            save_image(img_url, nid)
        if i % 10 == 0:
            print('image process : ' + str(i) + '/' + str(length))


def get_news_from_api():
    """
    通过接口获取news列表
    news包含字段(nid, time, label, title, doc, img_url)
    :return: news
    """
    news = []
    json_str = http_utils.get_data_from_url(NEWS_API)
    data = json.loads(json_str)
    results = data["value"]
    for result in results:
        nid = result.get('id')
        img_url = result.get('bigPic')
        time = result.get('transferTime')
        label = result.get('secondLable')
        title = result.get('headLine')
        doc = result.get('dataContent')
        news.append((nid, time, label, title, doc, img_url))
    return news


def save_image(img_url, file_name, file_path='images'):
    """
    保存单张图片
    :param img_url:
    :param file_name:
    :param file_path:
    :return:
    """
    # 保存图片到磁盘文件夹 file_path中，默认为当前脚本运行目录下的images文件夹
    try:
        if not os.path.exists(file_path):
            print('文件夹', file_path, '不存在，重新建立')
            # os.mkdir(file_path)
            os.makedirs(file_path)
        # 获得图片后缀
        if 'jpeg' in img_url:
            file_suffix = '.jpeg'
        elif 'jpg' in img_url:
            file_suffix = '.jpg'
        elif 'png' in img_url:
            file_suffix = '.png'
        else:
            file_suffix = '.jpeg'
        # 拼接图片名（包含路径）
        filename = '{}{}{}{}'.format(file_path, os.path.sep, file_name, file_suffix)
        # 下载图片，并保存到文件夹中
        cat_img = http_utils.get_data_from_url(img_url)
        with open(filename, 'wb') as f:
            f.write(cat_img)
    except IOError as e:
        print('文件操作失败', e)
    except Exception as e:
        print('错误 ：', e)


if __name__ == '__main__':
    main()
