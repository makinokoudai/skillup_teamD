import sys
from sqlalchemy import Column, Integer, VARCHAR
from database import Base
from database import ENGIN

class MstMerchandise(Base):
    __tablename__ = 'mst_merchandise'
    # 商品ID
    id = Column('id', VARCHAR(10), primary_key = True)
    # 商品名
    name = Column('name', VARCHAR(20))
    # 貨幣の種類
    price = Column('price', Integer)
    
    

def main(args):
    Base.metadata.create_all(bind=ENGIN)

if __name__ == '__main__':
    main(sys.argv)