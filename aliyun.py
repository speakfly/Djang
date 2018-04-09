import pymysql

conn = pymysql.connect(host='120.79.227.149',port=3306,user='huicong',password='huicong',db='rhs')

cursor = conn.cursor()
cursor.execute("select * from app_user ")

row_1 = cursor.fetchone()
print(row_1)
conn.commit()
cursor.close()
conn.close()
