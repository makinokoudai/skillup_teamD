from database import session
from datetime import date, datetime
from tables_transport import Transport
import sys
args = sys.argv
t = args[1]
seq = int(args[2])
departure = args[3]
arrival = args[4]
via = args[5]
amount = int(args[6])


# 登録するデータの編集
transport = Transport(
    date = t,
    seq = int(args[2]),
    departure = args[3],
    arrival = args[4],
    via = args[5],
    amount = int(args[6])
)
# INSERT処理
session.add(transport)
try:
# コミット
    session.commit()
    # 出力
    print("交通費精算テーブルにデータを登録しました")

except:
    print("error:交通費精算テーブルにデータを登録できませんでした")

