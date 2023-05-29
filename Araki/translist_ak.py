from database import session
from table import Transport
import sys
import os

#変数代入、パス生成
args = sys.argv
file_name = args[1]
path = os.path.join("..", "..", "file", file_name)

#データ取得
transport_list = session.query(Transport).all()

#ファイルの編集
file = open(path, mode="w", encoding="utf-8")
for value in transport_list:
    file.write(value.date+","+value.seq+","+value.depature+","+value.arrival+","+value.via+","+value.amount+"\n")
