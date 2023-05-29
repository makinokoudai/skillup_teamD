import sqlalchemy
from database import session
from tables import Stations
import sys

args = sys.argv
# 引数を変数sta1,sta2にそれぞれ代入
sta1 = args[1]
sta2 = args[2]
# テーブルstationsにおいて、nameの値（sta1,sta2）を指定し、対応するkiloの値を抽出
kilo1 = session.query(Stations.kilo).filter_by(name=sta1).first()
kilo2 = session.query(Stations.kilo).filter_by(name=sta2).first()
# 駅間計算（絶対値で出力）
if kilo1[0] < kilo2[0]: # kilo1-kilo2が負の値になるときの処理
    d = (kilo1[0] - kilo2[0]) * -1
    print('{:.2f}'.format(d),end="") # 少数第二位までを出力
else:
    d = kilo1[0] - kilo2[0]
    print('{:.2f}'.format(d),end="")

