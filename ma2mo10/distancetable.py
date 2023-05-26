import sys
from sqlalchemy import Column, Integer, DECIMAL, VARCHAR
from DB.database import Base
from DB.database import ENGIN

class DistanceTable(Base):
    __tablename__ = 'distance_table'
    seq = Column('seq', Integer, primary_key = True)
    name = Column('name', VARCHAR(20))
    kilo = Column('kilo', DECIMAL(6, 2))

def main(args):
    Base.metadata.create_all(bind=ENGIN)

if __name__ == '__main__':
    main(sys.argv)