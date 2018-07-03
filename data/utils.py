#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : pureoym
# @Contact : pureoym@163.com
# @TIME    : 2018/7/3 14:33
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


def remove_html_tag(input_str):
    """
    去除文本中的p标签
    :param input_str:
    :return:
    """
    return input_str.replace('<p>', '').replace('</p>', '')


def remove_extra_spaces(input_str):
    """
    去除多余的空格
    :param input_str:
    :return:
    """
    tmp = input_str.split()
    output_str = ' '.join(tmp)
    return output_str


def remove_empty_paragraph(input_str):
    """
    去除空段落
    :param input_str:
    :return:
    """
    return input_str.replace('<p></p>', '').replace('<p> </p>', '')


def generate_paragraph_head(input_str):
    """
    生成段首。生成逻辑<p>加四个英文空格
    :param input_str:
    :return:
    """
    return input_str.replace('<p> ', '<p>').replace('<p>', '<p>    ')


def map_full_width_to_half_width(input_str):
    """
    全角转半角
    :param input_str:
    :return:
    """
    output_str = ""
    for input_char in input_str:
        inside_code = ord(input_char)
        if inside_code == 12288:  # 全角空格直接转换
            inside_code = 32
        elif (inside_code >= 65313 and inside_code <= 65370) or \
                (inside_code >= 65296 and inside_code <= 65305):  # 全角字符（除空格）根据关系转化
            inside_code -= 65248
        output_str += chr(inside_code)
    return output_str


def cht_to_chs(input_str):
    pass


def chs_to_cht(input_str):
    pass


def chinese_clean(content):
    # print('input='+content)
    # content = remove_html_tag(content)
    content = map_full_width_to_half_width(content)
    content = remove_extra_spaces(content)
    content = remove_empty_paragraph(content)
    content = generate_paragraph_head(content)
    # print('output=' + content)
    return content
