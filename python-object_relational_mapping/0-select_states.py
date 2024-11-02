#!/usr/bin/python3
"""Module that lists all states from database 
after connecting to MySQL server running on localhost
at port 3306 to access database hbtn_0e_0_usa"""

import MySQLdb
from sys import argv


if __name__=="__main__":


    """ 
    Args: 
        mysql_username: user = sys.argv[1],
        mysql_password: passwd = sys.argv[2],
        database_name: db = sys.argv[3],

    Return:
        returns all states from databse hbtn_0e_0_usa,
        sorted in ascending order by states.id
    """

    with MySQLdb.connect(
        host="localhost", port=3306,
        user=argv[1], passwd=argv[2], db=argv[3]) as db:

        # ensuring query executes well  by using cursor object
        cursor = db.cursor()
        cursor.execute("SELECT * FROM states ORDER BY states.id ASC")

        for state in cursor.fetchall():
            print(state)
