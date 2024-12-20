#!/usr/bin/python3
"""
Module that retrieves the state name which is safe of any MySQL injections

After connecting to MySQL server running on localhost
at port 3306 to access database hbtn_0e_0_usa,
it returns the state name wich is safe of any MySQL injections

Usage:
    python3 3-my_safe_filter_states.py
    <mysql_username> <mysql_password> <database_name> <safe_state_name>

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


if __name__ == "__main__":
    """Main entry point"""

    username = argv[1]
    password = argv[2]
    database_name = argv[3]
    state_name_searched = argv[4]

    with MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database_name
    ) as db:

        with db.cursor() as cursor:
            query = """SELECT * FROM states
                    WHERE name = %s
                    ORDER BY states.id ASC"""
            cursor.execute(query, (argv[4],))

            states = cursor.fetchall()
            for state in states:
                print(state)
