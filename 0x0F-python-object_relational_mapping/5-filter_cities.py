#!/usr/bin/python3
"""
script that takes in the name of a state as an argument and
lists all cities of that state, using the database hbtn_0e_4_usa
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':

    user = argv[1]
    password = argv[2]
    database = argv[3]
    match = (argv[4], )

    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3]
            )

    cursor = db.cursor()
    cursor.execute("""SELECT cities.id, cities.name, states.name
    FROM cities INNER JOIN states ON cities.state_id = states.id
    WHERE states.name=%s
    ORDER BY cities.id ASC""", match)
    rows = cursor.fetchall()
    for row in rows:
        print(", ".join([row[1]]))
    cursor.close()
    db.close()
