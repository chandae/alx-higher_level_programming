#!/usr/bin/python3
""" lists all states from the database hbtn_0e_0_usa """
import MySQLdb
import sys


if __name__ == '__main__':
    # fetch cmdline arguments database username, password, db_name
    username, password, db_name = sys.argv[1:]
    db = MySQLdb.connect(user=username, passwd=password, db=db_name, port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    for query in cur.fetchall():
        print(query)
    cur.close()
    db.close()
