import vend_module.MY_input as MYin
import vend_module.MY_param as param
from DB.database import session
from DB.mst_merchandise import MstMerchandise
from   typing import Tuple

def display_item_db() -> None:
    '''DBに格納されている商品リストの表示'''
    item_list = session.query(MstMerchandise)
    #商品リストを表示
    #for item in param.const.item_dict:
        #print(f"{item}：{param.const.item_dict[item]}円")
    print(item_list)



def set_item() -> Tuple[int, str]:
    '''入力された商品と金額を格納してして返す'''
    #金額の入力を受け付ける
    money = MYin.input_money()
    #商品名/cancelの入力を受け付ける
    item_name = MYin.input_item(money)

    return money, item_name

display_item_db()