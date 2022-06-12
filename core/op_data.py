import os
from conf.setting import SQL_PATH,mysql_info
from core.tools import mysql
from core.tools import write_log
import time
def get_mysql_info():
    user = mysql_info.get('user')
    password = mysql_info.get('password')
    host = mysql_info.get('host')
    port = mysql_info.get('port')
    db = mysql_info.get('db')
    return user,password,host,port,db

# 数据库备份
def bak_db():
    user,password,host,port,db = get_mysql_info()
    filename = db + "_"+time.strftime("%Y%m%d%H%M%S")+".sql"
    sql_file_path = os.path.join(SQL_PATH,filename)

    command = 'mysqldump -u{user} -p{password} -P{port} -h{host} {db} >{file}'.format(
        user = user,password =password,port =port,host=host,db =db,file=sql_file_path
    )
    os.system(command)
    write_log("数据库%s备份到%s里了"%(db,sql_file_path))
    return sql_file_path

# 数据库恢复
def recover_db(sql_file_path):
    user,password,host,port,db = get_mysql_info()

    # sql1 = "drop database %s"%db
    # mysql.excute_one(sql1)

    # sql1 = "rename database %s to %s;"%(db,new_db)
    # print(sql1)
    # mysql.excute_one(sql1)
    #write_log("数据库%s改名为%s "%(db,new_db))
    new_db = db +"_"+time.strftime("%Y%m%d%H%M%S")
    
    sql2 = "create database %s charset utf8;"%new_db
    mysql.excute_one(sql2)
    write_log("%s数据库创建完成"%db)

    command = 'mysql -u{user} -p{password} -P{port} -h{host} {db} <{file}'.format(
        user = user,password =password,port =port,host=host,db =new_db,file=sql_file_path
    )
    os.system(command)
    write_log("%s数据库恢复完成！"%db)


if __name__ == "__main__":
    filepath = bak_db()
    recover_db(filepath)




















