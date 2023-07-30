#!/usr/bin/python3
"""
    List all states from a given db sorted in ascending order by id
    Username, password, and database names are given as user args
"""
import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(user='chandae',
                         passwd='$chandae@void()',
                         db='hbtn_0e_0_usa',
                         host='ff93ce7b7724.f1f47d6a.alx-cod.online'
                        )
    cur = db.cursor()
    cur.execute("SELECT id, name FROM states ORDER BY id ASC")
    allStates = cur.fetchall()

    for state in allStates:
        print(state)

    cur.close()
    db.close()
