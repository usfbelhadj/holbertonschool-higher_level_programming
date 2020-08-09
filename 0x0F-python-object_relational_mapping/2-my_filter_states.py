#!/usr/bin/python3
"""
script that takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument.
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':

    user = argv[1]
    password = argv[2]
    database = argv[3]
    match = argv[4]

    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3]
            )

    cursor = db.cursor()
    cursor.execute("""SELECT * FROM states WHERE BINARY match ='{}'
                    ORDER BY id""".format(match))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
