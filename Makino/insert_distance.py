from DB.database import session
from distancedb import StationsTable 
from typing import Dict

station_dict:Dict[str, float] = {"東京":0.00, "品川":6.78, "新横浜":25.54, "名古屋":342.02, "京都":476.31, "新大阪":515.35}

i:int = 0

for station in station_dict:
    i += 1
    stationtable = StationsTable(
        seq = i,
        name = station,
        kilo = station_dict[station]
    )

    session.add(stationtable)
    session.commit()