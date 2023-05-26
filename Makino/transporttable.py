import sys
from sqlalchemy import Column,Integer,VARCHAR,DATE
from DB.database import Base
from DB.database import ENGIN

class TransportTable(Base):
    __tablename__ = 'transport'
    date = Column('data',DATE,primary_key = True)
    seq = Column('seq',Integer,primary_key = True)
    departure = Column('deparure',VARCHAR(20))
    arrival = Column("arrival",VARCHAR(20))
    via = Column("via",VARCHAR(40))
    amount = Column("amount",Integer)
    

def main(args):
    Base.metadata.create_all(bind=ENGIN)

if __name__ == '__main__':
    main(sys.argv)
    


