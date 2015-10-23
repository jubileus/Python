# coding=UTF-8

import pymysql

from util.base.format.base import s
from util.base.format.base import i

__author__ = 'jubileus'


# 连接数据库
def conn_db(host, user, passwd, db, port, charset):
    # 获取Connection
    conn = pymysql.connect(host=s(host), user=s(user), passwd=s(passwd), db=s(db), port=i(port),
                           charset=s(charset))
    # 获取Cursor
    cur = conn.cursor()
    return conn, cur


# 关闭数据库
def close_db(conn, cur):
    conn.close()
    cur.close()


# 查询
def query(cur, sql):
    cur.execute(sql)
    return cur.fetchall()


# 插入,更新,删除
def operate(conn, cur, sql):
    stat = cur.execute(sql)
    conn.commit()
    return stat


