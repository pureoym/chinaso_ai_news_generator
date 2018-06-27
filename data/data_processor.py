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

API = 'http://data.mgt.chinaso365.com/datasrv/1.0/resources/01257/search?' \
      'fields=id,bigPic&filters=EQS_thirdLable,突发事件|NES_bigPic,NULL' \
      '&pagestart=1&fetchsize=10'


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
    pass


if __name__ == '__main__':
    main()
