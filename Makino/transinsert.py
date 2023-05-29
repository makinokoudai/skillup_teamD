
import sys
from DB.database import session
from transporttable import TransportTable
from datetime import datetime


try:
    # --------------------------------------------

    # データの入力処理

    #日付の入力 文字列をデータ型に
    input_date =datetime.strptime(sys.argv[1],'%Y%m%d') 

    #seq 重複データ防止のキーを入力
    input_seq = int(sys.argv[2]) 

    #出発の駅名を入力
    input_start = str(sys.argv[3]) 

    #出発の駅名を入力
    input_finish = str(sys.argv[4]) 

    #経路を入力
    input_via = str(sys.argv[5]) 

    #金額を入力
    input_amount = int(sys.argv[6])  


    # --------------------------------------------


    tp_table = TransportTable()

    # データをTransportTableに渡す
    tp_table.date = input_date
    tp_table.seq = input_seq 
    tp_table.departure = input_start
    tp_table.arrival = input_finish
    tp_table.via = input_via
    tp_table.amount = input_amount
    
    session.add(tp_table)
    session.commit()
    
    
#正常に処理できなかったとき
except:
    print("error:交通費精算テーブルにデータを登録できませんでした")




