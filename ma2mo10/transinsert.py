import sys
from DB.database import session
from transport_table import Transport
from datetime import datetime

args = sys.argv

try:
    dt = datetime.strptime(args[1], '%Y%m%d') #文字列をdatetime型に変換
    seq_num:int = int(args[2])                # 連番
    departure_sta:str = args[3]               # 出発地
    arrival_sta:str = args[4]                 # 到着地
    vi:str = args[5]                          # 経由・利用交通機関
    trans_amount:int = int(args[6])           # 金額

    # テーブルにそれぞれの引数を挿入
    transport = Transport(
        date = dt,
        seq = seq_num,
        depature = departure_sta,
        arrival = arrival_sta,
        via = vi,
        amount = trans_amount
    )

    session.add(transport)
    session.commit()

# 正常に登録できなかったときにエラーメッセージを出力する
except:
    print("error:交通費精算テーブルにデータを登録できませんでした")
