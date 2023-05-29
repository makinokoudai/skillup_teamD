import sys
from sqlalchemy import Column, Integer, VARCHAR, Date
from DB.database import Base
from DB.database import ENGIN

class TblMessage(Base):
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