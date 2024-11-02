#!/usr/bin/python3
"""
Module that lists all states with a name starting with N

After connecting to MySQL server running on localhost
at port 3306 to access database hbtn_0e_0_usa,
it returns all states with a name starting with N (upper case)
sorted in ascending order by states.id

NB: cursor.close() and db.close() are ensured
by using with...as.. statement instead

Usage:
    python3 1-filter_states.py
    <mysql_username> <mysql_password> <database_name>

Args :
    mysql_username: argv[1]
    mysql_password: argv[2]
    database_name: argv[3]

Returns:
    Prints all states starting with a 'N' from the database
"""

import MySQLdb
from sys import argv


if __name__ == "__main__":
    """Main entry point"""


def connect_database(username, password, db_name):
    """
    Connects to the database using 3 args, returns MySQLdb.connection
    """
    return MySQLdb.connect(
        host="localhost", port=3306, user=username, passwd=password, db=db_name
    )


with connect_database(argv[1], argv[2], argv[3]) as db:
    with db.cursor() as cursor:
        cursor.execute(
            "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY states.id ASC"
        )

        for state in cursor.fetchall():
            print(state)
