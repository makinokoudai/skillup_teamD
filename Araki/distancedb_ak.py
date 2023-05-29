import sys
from decimal import Decimal, ROUND_HALF_UP
from database import session
from table import Staitions

args = sys.argv
station_name = args[1]
start_sta = session.query(Staitions.kilo).filter_by(name=station_name).first()
station_name = args[2]
end_sta = session.query(Staitions.kilo).filter_by(name=station_name).first()

dist = abs(end_sta[0] - start_sta[0])      

print(str(dist.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)), end="")