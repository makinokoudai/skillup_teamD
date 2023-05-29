from DB.database import session
from distancetable import DistanceTable
from typing import Dict

# 駅名と東京駅からの距離を格納した辞書
station_dict:Dict[str, float] = {"東京":0.00, "品川":6.78, "新横浜":25.54, "名古屋":342.02, "京都":476.31, "新大阪":515.35}

i:int = 0          # カウント変数

# forで辞書の要素を一つずつでテーブルに挿入する
for station in station_dict:
    i += 1
    stationtable = DistanceTable(
        seq = i,
        name = station,
        kilo = station_dict[station]
    )

    session.add(stationtable)
    session.commit()