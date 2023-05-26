import sys
from sqlalchemy import Column, Integer, DATE, VARCHAR
from DB.database import Base
from DB.database import ENGIN

class Transport(Base):
    __tablename__ = 'transport'
    date = Column('date', DATE, primary_key = True)
    seq = Column('seq', Integer, primary_key = True)
    depature = Column('departure', VARCHAR(20))
    arrival = Column('arrival', VARCHAR(20))
    via = Column('via', VARCHAR(40))
    amount = Column('amount', Integer)


def main(args):
    Base.metadata.create_all(bind=ENGIN)

if __name__ == '__main__':
    main(sys.argv)