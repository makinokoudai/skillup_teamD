import sys
from sqlalchemy import Column, Integer
from database import Base
from database import ENGIN

class MoneyTable(Base):
    __tablename__ = 'money_table'
    # 貨幣の種類
    price = Column('price', Integer, primary_key = True)
    # 枚数
    number = Column('number', Integer)


def main(args):
    Base.metadata.create_all(bind=ENGIN)

if __name__ == '__main__':
    main(sys.argv)