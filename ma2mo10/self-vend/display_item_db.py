import vend_module.MY_input as MYin
from DB.database import session
from DB.mst_merchandise import MstMerchandise

def display_item_db() -> None:
    '''DBに格納されている商品リストの表示'''
    item_list = session.query(MstMerchandise)
    #商品リストを表示
    for item in item_list:
        print(f"{item.name}：{item_list.price}円")