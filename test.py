import paramiko

# JumpServer 的 SSH 连接信息
jump_host = "116.233.198.158"
jump_port = 22
jump_username = "zhubowen"
jump_password = "asdzxc123"

# MySQL 服务器的连接信息
mysql_host = "rm-bp1nk3hhw06nx5xq0490.mysql.rds.aliyuncs.com"
mysql_port = 33061
mysql_username = "handyopen_t"
mysql_password = "G2ltiow1f2"
mysql_database = "handyopen_t"

# 创建 SSH 客户端
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# 连接到 JumpServer
client.connect(jump_host, port=jump_port, username=jump_username, password=jump_password)

# 创建 SSH 通道（端口转发）
jump_transport = client.get_transport()
jump_channel = jump_transport.open_channel("direct-tcpip", (mysql_host, mysql_port), ("localhost", mysql_port))

# 连接到 MySQL 数据库
mysql_client = paramiko.SSHClient()
mysql_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
mysql_client.connect("localhost", port=mysql_port, username=mysql_username, password=mysql_password, sock=jump_channel)

# 运行 MySQL 命令
stdin, stdout, stderr = mysql_client.exec_command("SELECT * FROM your_table")

# 获取查询结果
result = stdout.readlines()

# 打印结果
for row in result:
    print(row.strip())

# 关闭连接
mysql_client.close()
client.close()
