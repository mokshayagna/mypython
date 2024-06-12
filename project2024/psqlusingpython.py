import psycopg2

def read_rows_from_db1(sys_ip, dbname, uname, passwd, tablename):
    conn = None
    conn = psycopg2.connect(database=dbname, user=uname, host=sys_ip, password=passwd)
    cur = conn.cursor()

    sqlquery = "SELECT * FROM %s" % tablename
    cur.execute(sqlquery)

    rows = cur.fetchall()
    print(rows)
    print(len(rows))

    for temp in rows:
        print(temp)
    print("")

    conn.close()
    return

def read_rows_from_db2(sys_ip, dbname, uname, passwd, tablename):
    conn = None
    conn = psycopg2.connect(database=dbname, user=uname, host=sys_ip, password=passwd)
    cur = conn.cursor()

    sqlquery = "SELECT * FROM %s WHERE name='Bhagavan'" % tablename
    cur.execute(sqlquery)

    rows = cur.fetchall()
    print(rows)
    print(len(rows))
    for row in rows:
        print(row)
    conn.close()
    return

def insert_rows_to_db(sys_ip, dbname, uname, passwd, tablename):
    conn = None
    conn = psycopg2.connect(database=dbname, user=uname, host=sys_ip, password=passwd)
    cur = conn.cursor()

    sqlquery = "INSERT INTO %s (name, fullname, uid, gid, phone, hphone, address, email, status) VALUES ('Poonam', 'Ponnam', 1000, 1001, '888888', '', 'Bangalore', 'ponam@gmail.com', 'T')" % tablename

    cur.execute(sqlquery)
    conn.commit()
    conn.close()

def insert_multiple_rows_to_db(sys_ip, dbname, uname, passwd, tablename):
    conn = None
    conn = psycopg2.connect(database=dbname, user=uname, host=sys_ip, password=passwd)
    cur = conn.cursor()

    namedict = (
        {"name":"manvir", "fullname":"Manvir",   "uid":"100", "email":"Manvir@gmail.com"},
        {"name":"Kiran", "fullname":"Kiran",   "uid":"101", "email":"Kiran@gmail.com"},
        {"name":"sunila", "fullname":"Sunila",   "uid":"100", "email":"Sunila@gmail.com"},
        {"name":"Bhagavan", "fullname":"Bhagavan",   "uid":"100", "email":"Bhagavan@gmail.com"}
        )

    cur.executemany("INSERT INTO students_list(name, fullname, uid, email) VALUES (%(name)s, %(fullname)s, %(uid)s, %(email)s)", namedict)
    conn.commit()
    conn.close()
    return

def list_all_tables_by_db(sys_ip, dbname, uname, passwd):
    conn = None
    conn = psycopg2.connect(database=dbname, user=uname, host=sys_ip, password=passwd)
    cur = conn.cursor()

    cur.execute("""SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'""")
    for table in cur.fetchall():
        print(table)

    return 0

def delete_rows_from_db(db):
    conn = None
    conn = psycopg2.connect(database="auradb", user="bhagavan", host="127.0.0.1", password="jnjnuh")
    cur = conn.cursor()

    namedict = (
        {"type":"base ball", "color":"white",   "location":"south", "install_date":"2020-01-20"},
        {"type":"cricket",  "color":"white",   "location":"north", "install_date":"2020-01-20"},
        {"type":"tennis",   "color":"red",     "location":"west",  "install_date":"2020-08-10"}
        )

    cur.executemany("INSERT INTO playground(type, color, location, install_date) VALUES (%(type)s, %(color)s, %(location)s, %(install_date)s)", namedict)
    conn.commit()
    conn.close()
    return

def main():
    read_rows_from_db1("127.0.0.1", "gcontacts", "aura", "jnjnuh", "students_list")
    # insert_rows_to_db("127.0.0.1", "gcontacts", "aura", "jnjnuh", "students_list")
    # read_rows_from_db1("127.0.0.1", "gcontacts", "aura", "jnjnuh", "students_list")
    # insert_multiple_rows_to_db("127.0.0.1", "gcontacts", "aura", "jnjnuh", "students_list")
    # read_rows_from_db1("127.0.0.1", "gcontacts", "aura", "jnjnuh", "students_list")
    # list_all_tables_by_db("127.0.0.1", "gcontacts", "aura", "jnjnuh")
    return


if (__name__ == "__main__"):
    main()

