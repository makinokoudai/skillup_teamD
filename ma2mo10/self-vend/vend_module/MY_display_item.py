#商品の表示や何を購入するかの入力受付に関するモジュール
import MY_input as MYin
import MY_param as param
from   typing import Tuple

def display_item() -> None:
    '''商品の表示と入力モジュールの呼び出し'''
    #商品リストを表示
    for item in param.const.item_dict:
        print(f"{item}：{param.const.item_dict[item]}円")



def set_item() -> Tuple[int, str]:
    '''入力された商品と金額を格納してして返す'''
    #金額の入力を受け付ける
    money = MYin.input_money()
    #商品名/cancelの入力を受け付ける
    item_name = MYin.input_item(money)

    return money, item_name