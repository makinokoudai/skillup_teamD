from database import session
from tables_transport import Transport
import os
import sys
args = sys.argv

file_name = args[1]
# パスの生成
path = os.path.join("..", "..", "file", file_name)
# データベースからデータ抽出
transport_list = session.query(Transport).all()
# ファイル操作
with open (path, mode="w", encoding="utf=8") as t:
    for info in transport_list:
        t.write(f'"{info.date}","{info.seq}","{info.departure}","{info.arrival}","{info.via}","{info.amount}"\n')
    
