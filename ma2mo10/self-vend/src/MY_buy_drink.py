#商品の購入に関するモジュール
import MY_param as param
from MY_input import input_YorN
import MY_return_change as MYchange

def calc_balance(item_name:str, money:int) -> int:
    '''購入後の残金を計算'''
    return money - param.const.item_dict[item_name]

def judge_buy(balance:int) -> bool:
    '''残金で購入可能か判定'''
    return True if balance >= param.const.MIN_PRICE else False


def buy_drink(money:int):
    # 残金の計算
    balance = calc_balance(money)
    # 購入できるかの判定
    if judge_buy(balance) == True:
        # 残金を表示
        print(f"残金：{balance}")
        # 購入を続けるかの入力受付
        input_YorN()
    
    else:
        
