#!/usr/bin/python3
"""
Module that lists all the cities from the database hbtn_0e_4_usa

After connecting to MySQL server running on localhost
at port 3306 to access database hbtn_0e_0_usa,
it returns all the cities present in the DB.

Usage:
    python3 4-cities_by_state.py
    <mysql_username> <mysql_password> <database_name>

Args :
    mysql_username: argv[1]
    mysql_password: argv[2]
    database_name: argv[3]

Returns:
    Prints all the cities of DB sorted in ascending order
"""

import MySQLdb
from sys import argv


if __name__ == "__main__":
    """Main entry point"""

    username = argv[1]
    password = argv[2]
    database_name = argv[3]

    with MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database_name
    ) as db:

        with db.cursor() as cursor:
            cursor.execute("""SELECT * FROM cities ORDER BY cities.id ASC""")

            for city in cursor.fetchall():
                print(city)
