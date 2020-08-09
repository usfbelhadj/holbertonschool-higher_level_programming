#!/usr/bin/python3
"""
script that lists all State objects from the database hbtn_0e_6_usa
"""


import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":

    user = argv[1]
    password = argv[2]
    database = argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (user, password, database), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    states = session.query(State).order_by(State.id.asc()).all()

    for state in states:
        print("{}: {}".format(state.id, state.name))

    session.close()
