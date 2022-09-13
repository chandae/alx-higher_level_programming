#!/usr/bin/python3
"""
    List all states with a name that begins with 'N' from the given db
    Username, password, and database names are given as user args
"""
import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         host='localhost',
                         port=3306)
    cur = db.cursor()
    cur.execute("""SELECT id name FROM states
        WHERE name LIKE 'N%'
        ORDER BY id ASC
        """)
    allStates = cur.fetchall()

    for state in allStates:
        print(state)

    cur.close()
    db.close()
