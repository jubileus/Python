# coding=UTF-8
from util.base.db import mysql_util
from util.base.format.base import s, i

__author__ = 'jubileus'


class User:
    # 定义基本属性
    id = 0
    name = ''
    age = 0

    # 定义方法

    def __init__(self, _name, _age=0, _id=0):
        self.id = _id
        self.name = _name
        self.age = _age

    def info(self):
        print('ID:{_id},  Age:{_age},  Name:{_name}'.format(_id=s(self.id).rjust(5), _name=s(self.name),
                                                            _age=s(self.age).rjust(3)))

    # 查询用户列表（全部用户）
    @staticmethod
    def get_all(cur):
        result = mysql_util.query(cur, 'SELECT * FROM t_user')
        u_list = []
        for u in result:
            usr = User(u[1], u[2], u[0])
            u_list.append(usr)
        return u_list

    # 查询id查询单个用户
    @staticmethod
    def get_by_id(cur, id):
        result = mysql_util.query(cur, 'SELECT * FROM t_user WHERE id = {_id}'.format(_id=id))
        if len(result) > 0:
            u = result[0]
            return User(u[1], u[2], u[0])
        else:
            return None

    # 根据sql更新用户
    @staticmethod
    def execute_sql(conn, cur, sql):
        return mysql_util.operate(conn, cur, sql)

    # 批量添加用户
    @staticmethod
    def batch_insert(conn, cur, users):
        sql = "INSERT INTO t_user (name, age) VALUES "
        for i in range(len(users)):
            u_name = users[i].name
            u_age = users[i].age
            sql += "('{}','{}')".format(u_name, u_age) if i == len(users)-1 else "('{}','{}'),".format(u_name, u_age)
        return mysql_util.operate(conn, cur, sql)

    # 保存至数据库
    def save_user(self, conn, cur):
        sql = "INSERT INTO t_user (name, age) VALUES ('{_name}','{_age}')".format(_name=self.name, _age=self.age)
        return mysql_util.operate(conn, cur, sql)

    # 从数据库删除
    def delete_user(self, conn, cur):
        sql = "DELETE FROM t_user WHERE id = {_id}".format(_id=self.id)
        return mysql_util.operate(conn, cur, sql)

    # 修改用户属性
    def modify_user(self, conn, cur):
        sql = "UPDATE t_user SET name = '{_name}', age = '{_age}' WHERE id = {_id}".format(_name=s(self.name),
                                                                                           _age=i(self.age),
                                                                                           _id=i(self.id))
        return mysql_util.operate(conn, cur, sql)
