from database import session
from mst_merchandise import MstMerchandise
from typing import Dict

item_dict:Dict[str, int] = {"お茶":110, "コーヒー":100, "ソーダ":160, "コーンポタージュ":130}
cnt:int = 1

for item_name in item_dict:
    mst_merchandise = MstMerchandise(
        id = 'F{:0=9}'.format(cnt),
        name = item_name,
        price = item_dict[item_name]
    )

    session.add(mst_merchandise)
    session.commit()
    cnt += 1