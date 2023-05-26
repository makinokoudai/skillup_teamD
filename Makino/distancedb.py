
import sys
from decimal import Decimal, ROUND_HALF_UP
from DB.database import session
from distancetable import StationsTable

first_station = sys.argv[1]
second_station = sys.argv[2]

distance = 0

try:
    start = session.query(StationsTable.kilo).filter_by(name = first_station).first()
    finish = session.query(StationsTable.kilo).filter_by(name = second_station).first()
    
    if start > finish:
        distance = start[0] - finish[0]
    else :
        distance = finish[0] - start[0]
        
    print(distance.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP),end="")
    
except KeyError:
    print("のぞみの停車駅を引数に設定してください", end="")


