#process_youyuan_mysql.py

# -*- coding: utf-8 -*-

import json
import redis
import pymysql


def main():

    # 指定redis数据库信息
    rediscli = redis.StrictRedis(host='127.0.0.1', port = 6379, db = 5)
    # 指定mysql数据库
    mysqlcli = pymysql.connect(host='127.0.0.1', user='root', passwd='123', db = 'test1', port=3306, use_unicode=True)

    while True:
        # FIFO模式为 blpop，LIFO模式为 brpop，获取键值
        source, data = rediscli.blpop(["ber:items"])

        # try:
        item = json.loads(data.decode())
        # 打印 source和item的数据
        print("source=======", source)
        print("item=========", item)

        # except Exception as e:
        #         print("类型错误", e)

        try:
            # 判断是否有重复教授，有的话，分开执行sql语句
            if (',' in item['instructor']):
                for i in str(item['instructor']).split(','):
                    cur = mysqlcli.cursor()
                    sql = "insert into clt_easya1(dept, name, course_title,course_number, units, type, time, week, location_url, introduce, info, instructor, location, school) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                    cur.execute(sql,
                                 [item['dept'], item['name'], item['course_title'], item['course_number'], item['units'],
                                 item['type'], item['time'], item['week'], item['location_url'], item['introduce'],
                                 item['info'], i, item['location'], item['school']])

                    # 提交sql事务
                    mysqlcli.commit()
                    # 关闭本次操作
                    cur.close()

            else:
                cur = mysqlcli.cursor()
                sql = "insert into clt_easya1(dept, name, course_title,course_number, units, type, time, week, location_url, introduce, info, instructor, location, school) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                cur.execute(sql,
                             [item['dept'], item['name'], item['course_title'], item['course_number'], item['units'],
                             item['type'], item['time'], item['week'], item['location_url'], item['introduce'],
                             item['info'], item['instructor'], item['location'], item['school']])

                # 提交sql事务
                mysqlcli.commit()
                # 关闭本次操作
                cur.close()

            ''' 
            # 使用cursor()方法获取操作游标
            cur = mysqlcli.cursor()
            sql = "insert into clt_easya2(dept, name, course_title,course_number, units, type, time, week, location_url, introduce, info, instructor, location, school) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            # 使用execute方法执行SQL INSERT语句
            cur.execute(sql,
                         [item['dept'], item['name'], item['course_title'], item['course_number'], item['units'],
                         item['type'], item['time'], item['week'], item['location_url'], item['introduce'],
                         item['info'], item['instructor'], item['location'], item['school']])
            mysqlcli.commit()

            # 关闭本次操作
            cur.close()
            # print("inserted %s" % item['source_url'])
            '''
        except (pymysql.Error, KeyError) as e:
            # 打印错误内容
            # print("Mysql Error %d: %s" % (e.args[0], e.args[1]))
            print(e)
            # print("插入数据错误", e)

if __name__ == '__main__':
    main()
