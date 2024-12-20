#!/usr/bin/python3
"""
Module that takes the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usa

After connecting to MySQL server running on localhost
at port 3306 to access database hbtn_0e_4_usa,
it returns all the cities of a defined state.

Usage:
    python3 5-filter_cities.py
    <mysql_username> <mysql_password> <database_name>

Args :
    mysql_username: argv[1]
    mysql_password: argv[2]
    database_name: argv[3]
    state_name: argv[4]

Returns:
    Prints all the cities of a defined state
    of the DB sorted in ascending order
"""

import MySQLdb
from sys import argv


if __name__ == "__main__":
    """Main entry point"""

    username = argv[1]
    password = argv[2]
    database_name = argv[3]
    state_name = argv[4]

    with MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database_name
    ) as db:

        with db.cursor() as cursor:
            query = """SELECT cities.name
                           FROM cities
                           JOIN states ON cities.state_id = states.id
                           WHERE states.name = %s
                           ORDER BY cities.id ASC;"""
            cursor.execute(query, (argv[4],))

            cities = cursor.fetchall()
            city_names = (name for (name,) in cities)
            output = ", ".join(city_names)
            print(output)
