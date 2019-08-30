import pymysql
import time

def main():

    mysqlcli = pymysql.connect(host='127.0.0.1', user='root', passwd='123', db='test1', port=3306, use_unicode=True)
    cur = mysqlcli.cursor()
    # 根据教授名称和课程名称进行筛选，并以“|”进行合并
    sql = "SELECT *,GROUP_CONCAT(time SEPARATOR'|'),group_concat(location_url separator'|'),group_concat(week separator'|'),group_concat(location separator'|'),group_concat(info separator'|') into outfile 'D:/ber.xls' from clt_easya1 GROUP BY course_title, course_number,instructor;"
    # 使用execute方法执行SQL INSERT语句
    cur.execute(sql)
    # 提交sql事务
    mysqlcli.commit()

    # 关闭本次操作
    cur.close()


if __name__ == '__main__':
    main()
