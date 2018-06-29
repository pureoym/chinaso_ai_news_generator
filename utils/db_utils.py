#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : pureoym
# @Contact : pureoym@163.com
# @TIME    : 2018/6/29 11:00
# @File    : db_utils.py
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
import sys
import MySQLdb
import logging

logger = logging.getLogger(__name__)


def get_mysql_conn(conf):
    '''
    建立mysql连接
    :param conf:
    :return:
    '''
    try:
        conn = pymysql.connect(host=conf['host'],
                               user=conf['user'],
                               passwd=conf['passwd'],
                               db=conf['db'],
                               port=conf['port'],
                               charset="utf8")
        logger.debug('mysql connection established')
    except Exception, e:
        logger.error(e)
        sys.exit()
    return conn


def get_mysql_data(conn, sql):
    '''
    通过sql获取数据
    :param conn:
    :param sql:
    :return:
    '''
    cursor = conn.cursor()
    result = []
    try:
        cursor.execute(sql)
        rows = cursor.fetchall()
        result = rows
    except MySQLdb.Error, e:
        conn.rollback()
        logger.error(e)
    finally:
        cursor.close()
        return result


def execute_mysql_sql(conn, sql):
    '''
    执行sql，一般用于更新或者新建
    :param conn:
    :param sql:
    :return:
    '''
    cursor = conn.cursor()
    try:
        cursor.execute(sql)
        conn.commit()
    except MySQLdb.Error, e:
        conn.rollback()
        logger.error(e)
    finally:
        cursor.close()
