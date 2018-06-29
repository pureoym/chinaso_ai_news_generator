#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : pureoym
# @Contact : pureoym@163.com
# @TIME    : 2018/6/29 9:16
# @File    : http_utils.py
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
from urllib import request
from urllib.parse import quote
import string
import logging

logger = logging.getLogger(__name__)


def get_data_from_url(url):
    """
    通过URL获取响应数据，返回响应所读取的内容
    :param url:
    :return:
    """
    url2 = quote(url, safe=string.printable)
    response = request.urlopen(url2)
    data = response.read()
    return data

