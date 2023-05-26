import sys
from database import session # 1.データベースへの接続
from stations_tables import Stations # 2.テーブル定義
# 引数入力
args = sys.argv
sta1 = str(args[1])
sta2 = str(args[2])
# 入力された駅名の距離をとってくる
distance1 = session.query(Stations.kilo).filter_by(name = sta1).all()
distance2 = session.query(Stations.kilo).filter_by(name = sta2).all()
# タプルから距離の数値を取り出す
distance1 = distance1[0][0]
distance2 = distance2[0][0]
# 距離の計算
if distance1 > distance2:
    distance = distance1 - distance2
else:
    distance = distance2 - distance1

print(distance)