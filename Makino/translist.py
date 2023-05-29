from transporttable import TransportTable
from DB.database import session
import sys

tr_table = TransportTable()

table_info = session.query(TransportTable).all()

# ファイル名の入力
input_file_name = str(sys.argv[1])

# ファイルのパス
file_path = "../../output/"+input_file_name

    
    
with open(file_path,mode="w",encoding="utf-8") as f:
    for info in table_info:
        f.write(f"{info.date},{info.seq},{info.departure},{info.arrival},{info.via},{info.amount}\n")
    


