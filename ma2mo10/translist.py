import sys
from DB.database import session
from transport_table import Transport

args = sys.argv

# ファイル名の生成
filename = "../../output/" + args[1]

# テーブルを取得し格納
translist = session.query(Transport).all()

# ファイルに一行ずつテーブルのデータを書き込み
with open(filename, mode='w', encoding='utf-8') as f:
    for trans in translist:
        f.write(f'"{trans.date}","{trans.seq}","{trans.depature}","{trans.arrival}","{trans.via}","{trans.amount}"\n')
