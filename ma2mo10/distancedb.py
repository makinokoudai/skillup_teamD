import sys
from decimal import Decimal, ROUND_HALF_UP
from DB.database import session
from distancetable import DistanceTable


args = sys.argv           # コマンドライン引数(第2引数:出発駅、第3引数:到着駅)

dep_sta = args[1]         # 出発駅
arr_sta = args[2]         # 到着駅
distance = 0              # 距離


try:
    # DBから距離を取得
    dep = session.query(DistanceTable.kilo).filter_by(name=dep_sta).first()
    arr = session.query(DistanceTable.kilo).filter_by(name=arr_sta).first()
    
    # 出発駅と到着駅の東京駅からの距離を比較して距離の差を求める
    # type(dep) -> (Decimal('0.00'),)なので0番目を取り出して距離を計算
    if dep > arr:
        distance = dep[0] - arr[0]      
    else:
        distance = arr[0] - dep[0]

    # Decimal().quantize()で値を丸めて標準出力する
    print(distance.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP), end="")

# のぞみの停車駅以外が引数に与えられた場合の例外処理
except KeyError:
    print("のぞみの停車駅を引数に設定してください", end="")