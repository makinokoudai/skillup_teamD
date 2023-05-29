import sys
from sqlalchemy import Column, Integer, VARCHAR, Date
from database import Base
from database import ENGIN

class MoneyTable(Base):
    __tablename__ = 'tbl_mesage'
    # 
    seq = Column('seq', Integer, primary_key = True)
    #  
    message = Column('message', VARCHAR(100))
    # 
    datetime = Column('datetime', Date)
    

def main(args):
    Base.metadata.create_all(bind=ENGIN)

if __name__ == '__main__':
    main(sys.argv)