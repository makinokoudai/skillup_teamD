import sys
from sqlalchemy import Column, DATE, Integer, VARCHAR,DECIMAL
from database import Base
from database import ENGINE
#テーブル：Attendnumの定義
class Staitions(Base):
    __tablename__ = 'stations'  #テーブルが増える場合はclassを追加
    seq = Column('seq', Integer, primary_key = True)
    name = Column('name', VARCHAR(20))
    kilo = Column('kilo', DECIMAL(6, 2))

class Transport(Base):
    __tablename__ = 'transport'
    date = Column('date', DATE, primary_key = True)
    seq = Column('seq', Integer, primary_key = True)
    depature = Column('departure', VARCHAR(20))
    arrival = Column('arrival', VARCHAR(20))
    via = Column('via', VARCHAR(40))
    amount = Column('amount', Integer)

def main(args):
    Base.metadata.create_all(bind=ENGINE)

if __name__ == "__main__":
    main(sys.argv)
#データベースにテーブルが定義されていない場合生成される
