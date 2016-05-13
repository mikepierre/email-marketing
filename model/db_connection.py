import pymysql
conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='email-marketing')
cur = conn.cursor()