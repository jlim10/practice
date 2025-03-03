import mysql.connector

config = {
    'host':'localhost',
    'database':'test',
}

try:
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    
    
    # sql2= "insert into sangdata(code,sang,su,dan) values(10,'상품1',2,2000)"
    # cursor.execute(sql2)
    # connection.commit()
    
    # sql2="insert into sangdata values(%s,%s,%s,%s)"
    # sql2_data=('11','상품2',5,1000)
    # cursor.execute(sql2,sql2_data)
    # connection.commit()
    
    # sql3="update sangdata set sang=%s,su=%s,dan=%s where code=%s"
    # sql3_data='Python',7,7000,'11'
    # cursor.execute(sql3,sql3_data)
    # connection.commit()
    
    # sql4="delete from sangdata where code=%s"
    # cursor.execute(sql4,('10',))
    # connection.commit()
    
    # sql="select code, sang, su, dan from sangdata"
    # cursor.execute(sql)
    
    # for data in cursor.fetchall():
    #     print('%s %s %s %s'%data)
    
    # cursor.execute(sql)
    # for code, sang, su, dan in cursor:
    #     print(code, sang, su, dan)

    # sql="select count(*) from sangdata where code<3"
    # cursor.execute(sql)
    # print(cursor.fetchall())
    
    
except Exception as err:
    print(err)
finally:
    cursor.close()
    connection.close()


# connection = mysql.connector.connect(
#     host='localhost',
#     database='test'
# )

# if connection.is_connected():
#     db_info=connection.get_server_info()
#     print(f"MySQL Server Version: {db_info}")
    
#     cursor = connection.cursor()
#     # cursor.execute("insert into fritab(name, phone, addr) values('지구인','111-1111','종로')")
#     # cursor.execute("insert into fritab values('우주인','111-1111','종로')")
#     # connection.commit()
    
#     cursor.execute("select * from fritab")
#     a=cursor.fetchall()
#     print(a)
    
#     # cursor.execute("delete from fritab where addr='종로';")
#     # connection.commit()
    
#     # database_name=cursor.fetchone()
#     # print(f"Connected database: {database_name[0]}")
    
#     cursor.close()
#     connection.close()