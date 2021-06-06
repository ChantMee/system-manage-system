from my_library.tool import *

from my_library.tool import connect_to_mysql, get_SQL_statement, write_log

class get_account_inf():

    def confirm_account_password(self, account, password): #已测试
        # 0 账号不存在
        # -1 密码不正确
        # 账号密码匹配,返回identifier
        conn = connect_to_mysql()
        column = ['identifier', 'account', 'password']
        table_name = 'users'
        condition = ['account = "%s" or identifier = "%s";' % (account, account)]
        sql = get_SQL_statement.select(get_SQL_statement(), column, table_name, condition)
        state = conn.execute(sql)
        if state == () or (account != state[0][0] and account != state[0][1]):
            return 0
        else:
            state = state[0]
            if password != state[2]:
                return -1
            else:
                return state[0]

    def get_identifier(self, account):
        conn = connect_to_mysql()
        sql = get_SQL_statement.select(get_SQL_statement(),
                ['identifier'], 'users', ['account = "%s" or identifier = "%s"'%(account, account)])
        text = conn.execute(sql)
        text = text[0]
        return text[0]

    def is_opened_dual_auth(self, identifier):
        sql = get_SQL_statement.select(get_SQL_statement(), ['dual_authentication'], 'users', ['identifier = "%s"'%identifier])
        conn = connect_to_mysql()
        text = conn.execute(sql)
        text = text[0]
        return text[0]

    def get_identity(self, identifier):
        sql = get_SQL_statement.select(get_SQL_statement(), ['identity'], 'identity_inf', ['identifier = "%s"'%identifier])
        conn = connect_to_mysql()
        text = conn.execute(sql)
        text = text[0]
        return text[0]

    def identifier_exist(self, identifier):
        sql = get_SQL_statement.select(get_SQL_statement(), ['identifier'], 'identity_inf', ['identifier = "%s"'%identifier])
        conn = connect_to_mysql()
        text = conn.execute(sql)
        if text == ():
            return 0
        else:
            return identifier == text[0][0]

    def account_exist(self, account):
        sql = get_SQL_statement.select(get_SQL_statement(),
                ['account'], 'users', ['account = "%s"' % account])
        conn = connect_to_mysql()
        text = conn.execute(sql)
        if text == ():
            return 0
        else:
            return account == text[0][0]

    def account_banned(self, identifier):
        sql = get_SQL_statement.select(get_SQL_statement(),
                ['banned'], 'users', ['identifier = "%s"' % identifier])
        conn = connect_to_mysql()
        text = conn.execute(sql)
        text = text[0]
        return text[0]

    def get_consecutive_fail_num(self, identifier):
        sql = get_SQL_statement.select(get_SQL_statement(),
                ['num_consecutive_failure'], 'users', ['identifier = "%s"' %identifier])
        conn = connect_to_mysql()
        text = conn.execute(sql)
        text = text[0]
        return text[0]

    def account_is_banned(self, identifier):
        sql = get_SQL_statement.select(get_SQL_statement(),
                                       ['banned'], 'users', ['identifier = "%s"' % identifier])
        conn = connect_to_mysql()
        text = conn.execute(sql)
        text = text[0]
        return text[0]


class modify_account_inf(get_account_inf):

    def modify_fail_num(self, identifier, time=0): #已测试
        conn = connect_to_mysql()
        if time != 0:
            time = get_account_inf.get_consecutive_fail_num(get_account_inf(), identifier)
            time = time + 1
        else:
            time = -1
        sql = get_SQL_statement.update(get_SQL_statement(),
            'users', ['num_consecutive_failure = %d'%(time + 1)], ['account = "%s"'%identifier])
        conn.execute(sql)

    def modify_dual_auth_token(self, identifier, new_token):
        # 0 修改失败 1 修改成功
        is_opened = self.is_opened_dual_auth(identifier)
        if is_opened == 0:
            return 0
        sql = get_SQL_statement.update(get_SQL_statement(), 'dual_user', ['token = "%s"'%new_token], ['identifier = "%s"'%identifier])
        conn = connect_to_mysql()
        conn.execute(sql)
        return 1

    def change_dual_auth_state(self, identifier, state, token = None):
        # state 1 打开 0 关闭
        # 返回值 0 非法：已经打开或关闭 1打开/关闭成功
        is_opened = self.is_opened_dual_auth(identifier)
        if is_opened == state:
            return 0
        sql = get_SQL_statement.update(get_SQL_statement(), 'users', ['dual_authentication = %d'%state], ['identifier = "%s"'%identifier])
        conn = connect_to_mysql()
        conn.execute(sql)
        if state == 1:
            sql = get_SQL_statement.insert(get_SQL_statement(), 'dual_user', ['identifier', 'token'], ['"%s"'%identifier, '"%s"'%token])
            conn.execute(sql)
        else:
            sql = get_SQL_statement.delete(get_SQL_statement(), 'dual_user', ['identifier = "%s"'%identifier])
            conn.execute(sql)
        return 1

    def modify_account(self, identifier, new_account):
        modify_fields = ['account = "%s"'%new_account]
        condition = ['identifier = "%s"'%identifier]
        sql = get_SQL_statement.update(get_SQL_statement(), 'users', modify_fields, condition)
        conn = connect_to_mysql()
        conn.execute(sql)

    def modify_password(self, identifier, new_password):
        modify_fields = ['password = "%s"'%new_password]
        condition = ['identifier = "%s"'%identifier]
        sql = get_SQL_statement.update(get_SQL_statement(), 'users', modify_fields, condition)
        conn = connect_to_mysql()
        conn.execute(sql)


    def ban_unban_account(self, identifier, mode = 1): #已测试
        # mode 1 封禁 0 解封
        conn = connect_to_mysql()
        sql = get_SQL_statement.update(get_SQL_statement(),
                'users', ['banned = %d'%mode],
                ['account = "%s"' % identifier])
        conn.execute(sql)

    def add_account(self, identifier, account, password):
        column = ['identifier', 'account', 'password']
        value = ['"%s"'%identifier, '"%s"'%account, '"%s"'%password]
        sql = get_SQL_statement.insert(get_SQL_statement(), 'users', column, value)
        conn = connect_to_mysql()
        conn.execute(sql)

class authentication(write_log, modify_account_inf):

    def login(self, account, password): #已测试
        # 0 账号不存在
        # 1 密码错误
        # 2 账号被禁用
        # 3 登陆成功
        # 4 验证账号密码正确但是需要双重认证
        #
        #若验证成功，那么[1]返回是否开启双重认证，[2]返回唯一标识码
        if get_account_inf.account_exist(get_account_inf(), account):
            account = get_account_inf.get_identifier(get_account_inf(), account)
        identifier = account
        state = self.confirm_account_password(account, password)
        # 0 账号不存在
        # -1 密码不正确
        # 账号密码匹配,返回identifier
        if state == 0:
            signal = 0
        # elif state == -1:
        #     signal = 1
        else:
            # column = ['banned', 'dual_authentication', 'num_consecutive_failure']
            # condition = ['identifier = "%s"'%state]
            # sql = get_SQL_statement.select(get_SQL_statement(), column, 'users', condition)
            # text = conn.execute(sql)
            # text = text[0]
            is_banned = get_account_inf.account_is_banned(get_account_inf(), identifier)
            if is_banned == 1:
                signal = 2
            else:
                if state == -1:
                    signal = 1
                else:
                    signal = 3
                    is_open_dual_auth = get_account_inf.is_opened_dual_auth(get_account_inf(), identifier)
                    if is_open_dual_auth == 1:
                        signal = 4
        if signal == 1:
            self.modify_fail_num(account, 1)
            time = get_account_inf.get_consecutive_fail_num(get_account_inf(), account)
            if time >= 4:
                modify_account_inf.ban_unban_account(modify_account_inf(), account)

        elif signal == 3 or signal == 4:
            self.modify_fail_num(state, 0)

        if signal == 0:
            self.write_login(account, signal)
        else:
            # column = ['identifier']
            # condition = ['identifier = "%s"' % account]
            # sql = get_SQL_statement.select(get_SQL_statement(), column, 'users', condition)
            self.write_login(account, signal)
        return signal

    def dual_auth(self, identifier, token): #已测试
        # 1 正确 0 错误
        column = ['token']
        condition = ['identifier = "%s"'%identifier]
        sql = get_SQL_statement.select(get_SQL_statement(), column, 'dual_user', condition)
        conn = connect_to_mysql()
        text = conn.execute(sql)
        text = text[0]
        if text[0] == token:
            return 1
        else:
            return 0

class add_descr_member():
    def add_inentity(self, identifier, identity, permission_id = None):
        # 学生 老师 辅导员 门卫 管理员 超级管理员
        # 0	 1		2     3   4     5
        if permission_id == None:
            permission_id = identity
        column = ['identifier', 'identity', 'permission_id']
        value = ['"%s"'%identifier, '%d'%identity, '%d'%permission_id]
        sql = get_SQL_statement.insert(get_SQL_statement(), 'identity_inf', column, value)
        conn = connect_to_mysql()
        conn.execute(sql)

    def add_student(self, identifier, major_id, name, class_id, enrollment_time):
        # 1 添加成功 0 添加失败
        if get_account_inf.account_exist(get_account_inf(), identifier) or get_account_inf.identifier_exist(get_account_inf(), identifier):
            return 0
        column = ['identifier', 'major_id', 'name', 'class_id', 'enrollment_time']
        value = ['"%s"'%identifier, '%d'%major_id, '"%s"'%name, '%d'%class_id, '"%s"'%enrollment_time]
        sql = get_SQL_statement.insert(get_SQL_statement(), 'student_inf', column, value)
        conn = connect_to_mysql()
        conn.execute(sql)
        modify_account_inf.add_account(modify_account_inf(), identifier, identifier, identifier)
        self.add_inentity(identifier, 0)
        return 1

    def add_user_but_student(self, identifier, identity):
        # 1 添加成功 0 添加失败
        if get_account_inf.account_exist(get_account_inf(), identifier) or get_account_inf.identifier_exist(
                get_account_inf(), identifier):
            return 0
        column = ['identifier', 'account', 'password']
        value = ['"%s"'%identifier, '"%s"'%identifier, '"%s"'%identifier]
        sql = get_SQL_statement.insert(get_SQL_statement(), 'users', column, value)
        conn = connect_to_mysql()
        conn.execute(sql)
        self.add_inentity(identifier, identity)
        return 1


  # 插入学生数据（测试）
# n = input()
# n = int(n)
# for i in range(0, n):
#     identifier = input()
#     identifier = str(identifier)
#     major_id = input()
#     major_id = int(major_id)
#     name = input()
#     name = str(name)
#     class_id = input()
#     class_id = int(class_id)
#     enrollment_time = input()
#     enrollment_time = str(enrollment_time)
#     # print(identifier, major_id, name, class_id, enrollment_time)
#     add_descr_member.add_student(add_descr_member(), identifier, major_id, name, class_id, enrollment_time)

 # 插入非学生成员（测试）
# n = input()
# n = int(n)
# for i in range(0, n):
#     identifier = input()
#     identifier = str(identifier)
#     identity = input()
#     identity = int(identity)
#     add_descr_member.add_user_but_student(add_descr_member(), identifier, identity)

# print(get_account_inf.account_banned(get_account_inf(), 'admin'))