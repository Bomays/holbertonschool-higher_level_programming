#!/usr/bin/python3
"""
Module that prints the first State object from database hbtn_0e_6_usa,
via MySQLAlchemy
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

    state = session.query(State).order_by(State.id).first()

    if not state:
        print("Nothing")
    else:
        print("{}: {}".format(state.id, state.name))

    session.close()