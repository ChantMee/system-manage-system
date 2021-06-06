import pymysql

class connect_to_mysql():

    def __init__(self):
        self.__database_address = 'localhost'
        self.__database_account = 'root'
        self.__database_password = 'Muxy000468932.'
        self.__database_select = 'test'
        self.__start()

    def __start(self):
        self.__conn = pymysql.connect(self.__database_address,
                                    self.__database_account,
                                    self.__database_password,
                                    self.__database_select)
        self.__cur = self.__conn.cursor()

    def execute(self, sql): # 0：连接已关闭
        self.__start()
        self.__cur.execute(sql)
        self.__conn.commit()
        text = self.__cur.fetchall()
        self.__end()
        return text

    def __end(self): #0：连接已关闭 1：连接关闭成功
        self.__cur.close()
        self.__conn.close()

class get_SQL_statement():

    def select(self, column, table_name, conditions=None):
        sql = 'SELECT '
        len_column = len(column)
        len_column = int(len_column)
        for i in range(0, len_column):
            sql += column[i] + ", "[i == len_column - 1]
        sql += 'FROM ' + table_name
        if conditions is not None:
            sql += ' WHERE '
            len_conditions = len(conditions)
            len_conditions = int(len_conditions)
            for i in range(0, len_conditions):
                sql += conditions[i] + [" AND ", ""][i == len_conditions - 1]
        sql += ';'
        return sql

    def update(self, table_name, modify_fields, conditions=None):
        sql = 'UPDATE ' + table_name + ' SET '
        len_modify_fields = len(modify_fields)
        len_modify_fields = int(len_modify_fields)
        for i in range(0, len_modify_fields):
            sql += modify_fields[i] + [', ', ''][i == len_modify_fields - 1]
        if conditions is not None:
            sql += ' WHERE '
            len_conditions = len(conditions)
            len_conditions = int(len_conditions)
            for i in range(0, len_conditions):
                sql += conditions[i] + [" AND ", ""][i == len_conditions - 1]
        sql += ';'
        return sql

    def insert(self, table_name, column, value):
        sql = 'INSERT INTO ' + table_name + ' ('
        len_column = len(column)
        len_column = int(len_column)
        for i in range(0, len_column):
            sql += str(column[i]) + [', ',') '][i == len_column - 1]
        sql += 'VALUES ('
        len_value = len(value)
        for i in range(0, len_value):
            sql += str(value[i]) + [', ',');'][i == len_column - 1]
        return sql

    def delete(self, table_name, condition):
        sql = 'DELETE FROM %s WHERE '%table_name
        len_condition = len(condition)
        for i in range(0, len_condition):
            sql += condition[i] + [" and ", ";"][i == len_condition - 1]
        return sql

    def mult_select(self, column, table_name, conditions=None):
        sql = 'SELECT '
        len_column = len(column)
        len_column = int(len_column)
        for i in range(0, len_column):
            sql += column[i] + ", "[i == len_column - 1]
        sql += 'FROM '
        len_table_name = len(table_name)
        len_table_name = int(len_table_name)
        for i in range(0, len_table_name):
            sql += table_name[i] + ", "[i == len_table_name - 1]
        if conditions is not None:
            sql += ' WHERE '
            len_conditions = len(conditions)
            len_conditions = int(len_conditions)
            for i in range(0, len_conditions):
                sql += conditions[i] + [" AND ", ""][i == len_conditions - 1]
        sql += ';'
        return sql

class write_log():
    def write_login(self, identifier, signal): #已测试
        # 0 账号不存在
        # 1 密码错误
        # 2 账号被禁用
        # 以上三种不区分是否有双重认证
        # 3 登陆成功
        # 4 账号密码匹配但需要双重认证
        # 5 双重验证失败
        # 6 双重验证通过，登陆成功
        identity = -1
        if signal == 0:
            identity = -1

        if signal > 3:
            dual_auth = 1
        elif signal == 3:
            dual_auth = 0
        else:
            dual_auth = -1

        if signal == 3 or signal == 5:
            succeed = 1
        else:
            succeed = 0
        conn = connect_to_mysql()
        if signal != 0:
            column = ['identity']
            condition = ['identifier = "%s"' % identifier]
            sql = get_SQL_statement.select(get_SQL_statement(), column, 'identity_inf', condition)
            text = conn.execute(sql)
            if text != ():
                identity = text[0][0]
        # detail = ['账号不存在', '密码错误', '账号被禁用', '登陆成功', '双重验证未通过', '双重验证通过，登陆成功']
        column = ['identity', 'identifier', 'dual_authentication', 'succeed', 'detail']
        value = [identity, '"%s"'%identifier, dual_auth, succeed, signal]
        sql = get_SQL_statement.insert(get_SQL_statement(), 'login_log', column, value)
        conn.execute(sql)