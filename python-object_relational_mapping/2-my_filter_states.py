#!/usr/bin/python3
"""
Module that retrieves the state name which is safe of any MySQL injections

After connecting to MySQL server running on localhost
at port 3306 to access database hbtn_0e_0_usa,
it returns the state name wich is safe of any MySQL injections

Usage:
    python3 1-filter_states.py
    <mysql_username> <mysql_password> <database_name> <safe_name>

Args :
    mysql_username: argv[1]
    mysql_password: argv[2]
    database_name: argv[3]
    state_name_searched: argv[4]

Returns:
    Prints state which is safe of any MySQL injections
"""

import MySQLdb
from sys import argv


def connect_database(username, password, db_name):
    """
    Args:
        username (str): mysql username
        password (str): mysql password
        database_name (str): database name

    Returns:
        Returns MySQL connection to database
    """
    return MySQLdb.connect(
        host="localhost", port=3306, user=username, passwd=password, db=db_name
    )


if __name__ == "__main__":
    """Main entry point"""

    with connect_database(argv[1], argv[2], argv[3]) as db:
        with db.cursor() as cursor:
            cursor.execute("SELECT * FROM states WHERE name = %s", (argv[4],))

            for state in cursor.fetchall():
                print(state)
