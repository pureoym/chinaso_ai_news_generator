#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : pureoym
# @Contact : pureoym@163.com
# @TIME    : 2018/6/29 9:16
# @File    : utils.py
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


def get_data_from_api(url):
    """
    通过URL获取接口数据
    :param url:
    :return:
    """
    url2 = quote(url, safe=string.printable)
    response = request.urlopen(url2)
    json_str = response.read()
    return json_str
