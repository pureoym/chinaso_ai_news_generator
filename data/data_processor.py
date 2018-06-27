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
from urllib2 import urlopen
import json
import os

API = 'http://data.mgt.chinaso365.com/datasrv/1.0/resources/01257/search?' \
      'fields=id,bigPic&filters=EQS_thirdLable,突发事件|NES_bigPic,NULL' \
      '&pagestart=1&fetchsize=10000'


def main():
    image_process()


def image_process():
    """
    下载图片，并重命名图片。重命名方法：资源主键.jpg
    :return:
    """
    images = get_images_from_api()
    save_images(images)


def get_images_from_api():
    """
    通过接口获取 (资源ID，图片URL) 列表
    :return:
    """
    images = []
    response = urlopen(API)
    json_str = response.read()
    data = json.loads(json_str)
    results = data["value"]
    for result in results:
        rid = str(result.get('id'))
        url = result.get('bigPic')
        images.append((rid, url))
    return images


def save_images(images):
    """保存图片至本地"""
    for image in images:
        rid = image[0]
        url = image[1]
        save_image(url, rid)


def save_image(img_url, file_name, file_path='images'):
    """
    保存单张图片
    :param img_url:
    :param file_name:
    :param file_path:
    :return:
    """
    # 保存图片到磁盘文件夹 file_path中，默认为当前脚本运行目录下的 book\img文件夹
    try:
        if not os.path.exists(file_path):
            print '文件夹', file_path, '不存在，重新建立'
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
        response = urlopen(img_url)
        cat_img = response.read()
        with open(filename, 'wb') as f:
            f.write(cat_img)
    except IOError as e:
        print '文件操作失败', e
    except Exception as e:
        print '错误 ：', e


if __name__ == '__main__':
    main()
