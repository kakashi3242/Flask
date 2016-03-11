import pymysql


def mysql(sql):
    # 打开数据库连接
    db = pymysql.connect("127.0.0.1", "root", "123", "flask" )
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    # 插入固定字符
    # sql = "insert into USER (user_name, user_password) VALUES ('ww','111111')"
    # sql = "INSERT INTO ACTION_CODE (action_code) VALUES ('ii')"
    # 插入变量
    # sql = "INSERT INTO form (form_text) VALUES ('"+form_text+"')"
    # 选择指定字段
    # sql = "select user_password from USER WHERE user_name = '"+user_name+"'"
    # print(sql)
    cursor.execute(sql)
    result = cursor.fetchone()
    db.commit()
    print('SQL done!')
    # 关闭数据库连接
    db.close()
    return result

def insert(form_text, form_name):
    # 插入sql语句
    sql = "INSERT INTO form (form_text, form_name) VALUES ('"+form_text+"', '"+form_name+"')"

    mysql(sql)

def query(form_text):
    # 查询sql语句
    sql = "select form_name from form WHERE form_text like '"+form_text+"'"
    form_name = mysql(sql)
    for tup in form_name:
        return tup
    # print(form_name)


if __name__ == '__main__':
    query('JJ')
    # insert('JJ', 'Redick')



