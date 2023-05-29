import sys
from sqlalchemy import Column, Integer, VARCHAR
from DB.database import Base
from DB.database import ENGIN

class TblStock(Base):
    __tablename__ = 'tbl_stock'
    # 商品ID
    id = Column('id', VARCHAR(10), primary_key = True)
    # 在庫数 
    stock = Column('stock', Integer)
    
    

def main(args):
    Base.metadata.create_all(bind=ENGIN)

if __name__ == '__main__':
    main(sys.argv)