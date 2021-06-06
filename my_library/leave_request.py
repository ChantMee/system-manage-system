from my_library.tool import write_log, get_SQL_statement, connect_to_mysql
from my_library.user import *

class leave_inf():

    def is_withdrewed(self, request_id):
        sql = get_SQL_statement.select(get_SQL_statement(), ['withdraw'], 'leave_request', ['id = %d'%request_id])
        conn = connect_to_mysql()
        text = conn.execute(sql)
        text = text[0]
        return text[0]

    def is_approved(self, request_id):
        # 0 未阅 1 同意 2 拒绝
        sql = get_SQL_statement.select(get_SQL_statement(), ['approval'], 'leave_request', ['id = %d'%request_id])
        conn = connect_to_mysql()
        text = conn.execute(sql)
        text = text[0]
        return text[0]

    def read_by_teacher(self, request_id):
        sql = get_SQL_statement.select(get_SQL_statement(), ['read_by_teacher'], 'leave_request', ['id = "%d"'%request_id])
        conn = connect_to_mysql()
        text = conn.execute(sql)
        text = text[0]
        return text[0]

    def get_teacher_remark(self, request_id):
        sql = get_SQL_statement.select(get_SQL_statement(), ['teacher_remark'], 'leave_request_text', ['id = %d'%request_id])
        conn = connect_to_mysql()
        text = conn.execute(sql)
        text = text[0]
        return text[0]

    def get_approval_state(self, request_id):
        sql = get_SQL_statement.select(get_SQL_statement(), ['approval'], 'leave_request', ['id = %d'%request_id])
        conn = connect_to_mysql()
        text = conn.execute(sql)
        text = text[0]
        return text[0]

    def id_exist(self, id):
        sql = get_SQL_statement.select(get_SQL_statement(), ['approval'], 'leave_request', ['id = %d' % id])
        conn = connect_to_mysql()
        text = conn.execute(sql)
        return text != ()


class student(leave_inf):

    def __get_class_id(self, identifier):
        sql = get_SQL_statement.select(get_SQL_statement(), ['class_id'], 'student_inf', ['identifier = "%s"'%identifier])
        conn = connect_to_mysql()
        text = conn.execute(sql)
        text = text[0]
        return text[0]

    def withdraw_request(self, request_id):
        # 0 失败，该假条已撤回
        # 1 失败，该假条已被批准
        # 2 成功
        is_withdrewed = self.is_withdrewed(request_id)
        if is_withdrewed == 1:
            return 0
        is_approved = self.is_approved(request_id)
        if is_approved == 1:
            return 1
        sql = get_SQL_statement.update(get_SQL_statement(), 'leave_request', ['withdraw = 1'], ['id = %d'%request_id])
        conn = connect_to_mysql()
        conn.execute(sql)
        return 2

    def issue_request(self, identifier, leave_type, time_start, time_end, leave_reason):
        # 0 事假 1 病假
        class_id = self.__get_class_id(identifier)
        sql = get_SQL_statement.insert(get_SQL_statement(), 'leave_request',
                                       ['identifier', 'class_id', 'leave_type', 'time_start', 'time_end'],
                                       ['"%s"'%identifier, '%d'%class_id, '%d'%leave_type, '"%s"'%time_start, '"%s"'%time_end])
        conn = connect_to_mysql()
        conn.execute(sql)
        sql = get_SQL_statement.insert(get_SQL_statement(), 'leave_request_text', ['leave_reason'], ['"%s"'%leave_reason])
        conn.execute(sql)

    def get_request_list_simplify(self, identifier): # 这里需要用正则表达式提取出来
        # id 请假时间 请假类型 是否批准 开始时间 结束时间 是否撤回
        column = ['id', 'request_time', 'leave_type', 'approval', 'time_start', 'time_end', 'withdraw', 'read_by_teacher']
        sql = get_SQL_statement.select(get_SQL_statement(), column, 'leave_request', ['identifier = "%s"'%identifier])
        conn = connect_to_mysql()
        text = conn.execute(sql)
        return text

class teacher():

    def get_request_list(self, identifier):
        # id 是否撤回 是否已读 学号 请假类型 开始时间 结束时间 是否通过
        column = ['leave_request.id', 'leave_request.withdraw', 'read_by_teacher', 'leave_request.identifier', 'leave_request.leave_type',
                  'leave_request.time_start', 'leave_request.time_end', 'leave_request.approval']
        table_name = ['teacher_list', 'leave_request', 'student_inf']
        condition = ['leave_request.identifier = student_inf.identifier',
                     'student_inf.class_id = teacher_list.class_id',
                     'teacher_list.identifier = "%s"'%identifier]
        sql = get_SQL_statement.mult_select(get_SQL_statement(), column, table_name, condition)
        conn = connect_to_mysql()
        text = conn.execute(sql)
        return text

    def confirm_read(self, request_id):
        # 1 确认成功 0 确认失败
        is_read = leave_inf.read_by_teacher(leave_inf(), request_id)
        is_withdrewed = leave_inf.is_withdrewed(leave_inf(), request_id)
        is_approved = leave_inf.is_approved(leave_inf(), request_id)
        if is_read == 1 or is_withdrewed == 1 or is_approved == 2:
            return 0
        sql = get_SQL_statement.update(get_SQL_statement(), 'leave_request', ['read_by_teacher = 1'], ['id = %d'%request_id])
        conn = connect_to_mysql()
        conn.execute(sql)
        return 1

    def remark_request(self, request_id, remark):
        sql = get_SQL_statement.update(get_SQL_statement(), 'leave_request_text',
                                       ['teacher_remark = "%s"'%remark], ['id = "%s"'%request_id])
        conn = connect_to_mysql()
        conn.execute(sql)


class counselor():

    def get_request_list(self, identifier):
        # id 请假时间 是否撤回 学号 请假类型 开始时间 结束时间 是否同意 是否出校 是否返校
        column = ['leave_request.id', 'leave_request.request_time', 'leave_request.withdraw',
                  'leave_request.identifier', 'leave_request.leave_type', 'leave_request.time_start',
                  'leave_request.time_end', 'leave_request.approval',
                  'leave_request.out_school', 'leave_request.return_school']
        table_name = ['counselor_list', 'leave_request', 'student_inf']
        condition = ['leave_request.identifier = student_inf.identifier',
                     'student_inf.major_id = counselor_list.major_id',
                     'counselor_list.identifier = "%s"'%identifier]
        sql = get_SQL_statement.mult_select(get_SQL_statement(), column, table_name, condition)
        conn = connect_to_mysql()
        text = conn.execute(sql)
        return text

    def examine_request(self, request_id, result):
        sql = get_SQL_statement.update(get_SQL_statement(), 'leave_request', ['approval = %d'%result], ['id = %d'%request_id])
        conn = connect_to_mysql()
        conn.execute(sql)


#  插入请假请求（测试）
# n = input()
# n = int(n)
# for i in range(0, n):
#     identifier = input()
#     identifier = str(identifier)
#     leave_type = input()
#     leave_type = int(leave_type)
#     time_start = input()
#     time_start = str(time_start)
#     time_end = input()
#     time_end = str(time_end)
#     reason = input()
#     reason = str(reason)
#     student.issue_request(student(), identifier, leave_type, time_start, time_end, reason)


# counselor.get_request_list(counselor(), 'counselor')
# text = teacher.get_request_list(teacher(), 'teacher')
# text = student.get_request_list_simplify(student(), 'student')
# for i in text:
#     print(i)
# teacher.confirm_read(teacher(), 2)