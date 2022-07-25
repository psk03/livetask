import mysql.connector as conn

mydb = conn.connect(host = "localhost" , user = "root", passwd = "pranav3597")
cursor = mydb.cursor()
cursor.execute ("select employee_id, emp_mailid from sudhanshu.ineuron")
l = []
for i in cursor.fetchall():
    l.append(i)
    print(i)
print(type(l[0]))
