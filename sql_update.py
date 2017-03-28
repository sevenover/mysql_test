#!/usr/bin.env python
#coding:utf-8
import pymysql
conn = pymysql.connect(user='root',host='localhost', db='school')
cur = conn.cursor()
# 修改数据
sql='update school set name=%s where id=4'#使用sql语句,无论我们要插入的数据是什么类型,占位符都可以用%s  
params=('sb1')  
cur.execute(sql,params)  
conn.commit()

# 删除行
# sql='delete from school where id=%s'#使用sql语句,无论我们要插入的数据是什么类型,占位符都可以用%s  
# params=(2)  
# cur.execute(sql,params)  
# conn.commit()

cur.close()    
conn.close()