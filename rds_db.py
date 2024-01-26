import pymysql

conn = pymysql.connect(
    host="mysqldb.cd2pfftf5k62.us-east-2.rds.amazonaws.com",
    port=3306,
    user="admin",
    password="adminadmin",
    db="mysqldb"
)

def insert_details(name, age, city):
    cur = conn.cursor()
    cur.execute('CREATE DATABASE IF NOT EXISTS users')
    cur.execute("INSERT INTO user (username, age, city) VALUES (%s, %s, %s)", (name, age, city))
    conn.commit()

def get_details():
    cur = conn.cursor()
    cur.execute('CREATE DATABASE IF NOT EXISTS users')
    cur.execute("SELECT * FROM user")
    details = cur.fetchall()
    return details