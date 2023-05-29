import sys
import os
from database import session # 1.データベースへの接続
from transport_tables import Transport # 2.テーブル定義
args = sys.argv
path = os.path.join(".","output","output.txt") # パスを作成する

datalist = session.query(Transport).all() 

with open (path,mode="w",encoding="utf-8") as f: #ファイルを開く
    for i in datalist:
        f.write(f'"{i.date}", "{i.seq}", "{i.departure}","{i.arrival}","{i.via}","{i.amount}"\n') #ファイルに書き込み