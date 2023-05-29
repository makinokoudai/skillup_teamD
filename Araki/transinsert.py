import sys
from database import session
from table import Transport
from sqlalchemy import DATE
args = sys.argv

try:
    date_data = args[1]
    year = date_data // 10000
    month = (date_data - (year * 10000)) // 100
    day = date_data - (year * 10000) - (month * 100)

    dt = DATE(year,month,day)
    seq_ = int(args[2])
    departure_ = str(args[3])
    arrival_ = str(args[4])
    via_ = str(args[5])
    amount_ = int(args[6])

    transport = Transport(
        date = dt,
        seq = seq_,
        depature = departure_,
        arrival = arrival_,
        via = via_,
        amount = amount_
    )

    session.add(transport)
    session.commit()
    print("交通費精算テーブルにデータを登録しました",end="")

except:
    print("error:交通費精算テーブルにデータを登録できませんでした",end="")
