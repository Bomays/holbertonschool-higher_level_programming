#!/usr/bin/python3
"""
Module that lists all State objects that contains the letter 'a'
from database hbtn_0e_6_usa, via MySQLAlchemy
"""


from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    """Main entry point"""

    username = argv[1]
    password = argv[2]
    database_name = argv[3]

    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            argv[1], argv[2], argv[3]),
        pool_pre_ping=True,
    )
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).filter(State.name.like('%a%')).order_by(State.id).all()

    if not states:
        print("Nothing")
    else:
        for state in states:
            print("{}: {}".format(state.id, state.name))

    session.close()
