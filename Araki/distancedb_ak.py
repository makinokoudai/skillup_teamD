import sys
from decimal import Decimal, ROUND_HALF_UP
from database import session
from table import Staitions

#指定された数値の取得
args = sys.argv
station_name = args[1]
start_sta = session.query(Staitions.kilo).filter_by(name=station_name).first()
station_name = args[2]
end_sta = session.query(Staitions.kilo).filter_by(name=station_name).first()

#絶対値の算出
dist = abs(end_sta[0] - start_sta[0])      

#数値の小数点切り捨てと表示
print(str(dist.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)), end="")