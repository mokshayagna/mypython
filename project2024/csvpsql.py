import csv
import psycopg2
import sys

fd = open('/home/moksha/mypython/project2024/new_data.csv','rt')
reader = csv.reader(fd)

conn = None
conn = psycopg2.connect(database="gcontacts", user="aura", host="127.0.0.1", password="jnjnuh")
cur = conn.cursor()

i = 0
print(reader)
for row in reader:
    if(i==0):
        i = 1
        continue
    cur.execute("INSERT INTO students_list(name, fullname, uid, gid, phone, hphone, address, email, status) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", 
       (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], "1"))

conn.commit()

fd.close()

cur.execute("SELECT * FROM students_list")
rows = cur.fetchall()

for row in rows:
    print(row)
    