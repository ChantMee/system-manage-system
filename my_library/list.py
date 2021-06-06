from my_library.tool import connect_to_mysql, get_SQL_statement

class insert_extern_list():
    def insert_teacher_list(self, identifier, class_id):
        column = ['identifier', 'class_id']
        value = ['"%s"'%identifier, '%d'%class_id]
        sql = get_SQL_statement.insert(get_SQL_statement(), 'teacher_list', column, value)
        conn = connect_to_mysql()
        conn.execute(sql)

    def insert_counselor_list(self, identifier, major_id):
        column = ['identifier', 'major_id']
        value = ['"%s"'%identifier, '%d'%major_id]
        sql = get_SQL_statement.insert(get_SQL_statement(), 'counselor_list', column, value)
        conn = connect_to_mysql()
        conn.execute(sql)

    def insert_major_list(self, major_id, class_id):
        column = ['major_id', 'class_id']
        value = ['%d'%major_id, '%d'%class_id]
        sql = get_SQL_statement.insert(get_SQL_statement(), 'major_list', column, value)
        conn = connect_to_mysql()
        conn.execute(sql)


# 插入老师信息（测试）
# n = input()
# n = int(n)
# for i in range(0, n):
#     identifier = input()
#     identifier = str(identifier)
#     class_id = input()
#     class_id = int(class_id)
#     insert_extern_list.insert_teacher_list(insert_extern_list(), identifier, class_id)

# 插入辅导员信息（测试）
# n = input()
# n = int(n)
# for i in range(0, n):
#     identifier = input()
#     identifier = str(identifier)
#     major_id = input()
#     major_id = int(major_id)
#     insert_extern_list.insert_counselor_list(insert_extern_list(), identifier, major_id)

#插入专业信息（测试）
# n = input()
# n = int(n)
# for i in range(0, n):
#     major_id = input()
#     major_id = int(major_id)
#     class_id = input()
#     class_id = int(class_id)
#     insert_extern_list.insert_major_list(insert_extern_list(), major_id, class_id)