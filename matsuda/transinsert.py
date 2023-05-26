import sys
from datetime import date
from database import session # 1.データベースへの接続
from transport_tables import Transport # 2.テーブル定義

# 引数入力
args = sys.argv
d = args[1]
seq_num = int(args[2]) 
sta1 = str(args[3])
sta2 = str(args[4])
train = str(args[5])
money = int(args[6])

# 日付を分ける
year = d[:4]
month = d[4:6]
day = d[6:8]
dt = date(int(year),int(month),int(day))

try:
# テーブルにデータ追加
    table = Transport(
        date = dt,
        seq = seq_num,
        departure = sta1,
        arrival = sta2,
        via = train,
        amount = money
        )
    # INSERT処理
    session.add(table)
    # コミット
    session.commit()
except:
    print("交通費精算テーブルにデータを登録しました")


