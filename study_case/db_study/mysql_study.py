# coding=UTF-8
import traceback

from study_case.db_study.t_user import User
from util.base.db import mysql_util
from util.base.format.base import s

__author__ = 'jubileus'


# 测试:插入
def insert(conn, cur):
    user_1 = User('煤球', 33)
    stat = user_1.save_user(conn, cur)
    print('插入成功' if stat > 0 else '插入失败')


# 测试：批量插入
def batch_insert(conn, cur):
    users = []
    u1 = User('a', 11, 99)
    u2 = User('b', 12, 100)
    users.append(u1)
    users.append(u2)
    success = User.batch_insert(conn, cur, users)
    print('成功插入' + s(success) + '条用户数据')


# 测试:查询全部用户
def query(cur):
    user_list = User.get_all(cur)

    for user in user_list:
        user.info()

    # # ------- 用户对象列表转换为用户字典列表（间接得到用户列表json） S -------
    # for i in range(len(user_list)):
    #     user_list[i] = user_list[i].__dict__
    # print(user_list)
    # # ------- 用户对象列表转换为用户字典列表（间接得到用户列表json） E -------


# 测试:根据id查询用户
def get_single(cur, id):
    user = User.get_by_id(cur, id)
    return user


# 测试主方法
def main():
    try:
        # 连接数据库
        conn, cur = mysql_util.conn_db('192.168.1.33', 'python', '123', 'python', 3306, 'utf8')

        # # 插入示例
        # insert(conn, cur)

        # # 批量插入
        # batch_insert(conn, cur)

        # # 删除示例
        # user = get_single(cur, 3)
        # if user is not None:
        #     user.delete_user(conn, cur)
        #     print('删除成功')
        # else:
        #     print('用户为空')

        # # 更新示例
        # user = get_single(cur, 3)
        # if user is not None:
        #     user.age = 20
        #     user.name = 'Joker'
        #     user.modify_user(conn, cur)
        #     print('更新成功')
        # else:
        #     print('用户为空')

        # 查询示例
        query(cur)

        # 关闭数据库
        mysql_util.close_db(conn, cur)
    except Exception:
        traceback.print_exc()


main()
