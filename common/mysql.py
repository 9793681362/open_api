import pymysql

class Mysql:
    def __init__(self,sql):
        self.sql = sql

    def select_mysql(self):
        mysql_host = "jump.handyprint.cn"
        mysql_port = 33061
        mysql_username = "435b4ebd-e525-48c7-924c-3ef25367a656"
        mysql_password = "DKawl4xeI0P8QbHw"
        mysql_database = "handyopen_t"

        # 建立数据库连接
        connection = pymysql.connect(host=mysql_host, port=mysql_port, user=mysql_username, password=mysql_password,
                                     database=mysql_database)
        cur = connection.cursor()
        sql = self.sql
        cur.execute(sql)
        all_obj = cur.fetchall()
        cur.close()
        connection.close()
        for i in all_obj:
            return i



if __name__ == '__main__':
    # pass
    ls = Mysql("SELECT * FROM `order_prod` WHERE p_order_id = 19717").select_mysql()
    print(ls)



