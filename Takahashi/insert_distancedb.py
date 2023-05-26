from tables import Stations
from database import session

# 登録するデータの編集
stations = Stations(
    seq = 6,
    name = "新大阪",
    kilo = 515.35
)
# INSERT処理
session.add(stations)
# コミット
session.commit()