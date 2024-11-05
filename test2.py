import pymysql

# 配置数据库连接参数
mysql_host = "jump.handyprint.cn"
mysql_port = 33061
mysql_username = "dbc27d34-938a-4f65-bf40-4f9acccc5ec2"
mysql_password = "xELIHJMIP10GBCcY"
mysql_database = "handyopen_t"

# 建立数据库连接
connection = pymysql.connect(host=mysql_host, port=mysql_port, user=mysql_username, password=mysql_password, database=mysql_database)

# 创建游标对象
cursor = connection.cursor()

# 执行 SQL 查询
cursor.execute("SELECT * FROM `order_prod` WHERE p_order_id = 19717")

# 获取查询结果
result = cursor.fetchall()

# 打印结果
for row in result:
    print(row)

# 关闭游标和连接
cursor.close()
connection.close()
