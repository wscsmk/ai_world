import mysql.connector

import os

# 建立连接
conn = mysql.connector.connect(
    host="localhost",      # 数据库地址，本地为 localhost
    user="root",  # 用户名
    password=os.getenv('sql_password'),  # 密码
    database="your_db"     # 要使用的数据库名
)

# 创建游标，用于执行 SQL
cursor = conn.cursor()