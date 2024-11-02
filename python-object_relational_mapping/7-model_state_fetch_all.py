#!/usr/bin/python3
"""
Module that lists all the cities from database hbtn_0e_6_usa,
via MySQLAlchemy
"""


from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


username = argv[1]
password = argv[2]
database_name = argv[3]

if __name__ == "__main__":
    """Main entry point"""

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State).order_by(State.id).all():
        print('{}: {}'.format(state.id, state.name))

    session.close()
