#商品の購入に関するモジュール
import MY_param as param
from MY_input import input_YorN
import MY_return_change as MYchange
import MY_input as MYin

def calc_balance(item_name:str, money:int) -> int:
    '''購入後の残金を計算'''
    return money - param.const.item_dict[item_name]


def judge_buy(balance:int) -> bool:
    '''残金で購入可能か判定'''
    return True if balance >= param.const.MIN_PRICE else False

# 購入全体の処理
def buy_drink(item_name:str, balance:int) -> None:
    while True:
        # 残金の計算
        balance = calc_balance(item_name, balance)
        # 購入できるかの判定
        if judge_buy(balance) == True:
            # 残金を表示
            print(f"残金：{balance}")
            # 購入を続けるかの入力受付
            if input_YorN() == 'Y':
                item_name = MYin.input_item(balance)
            # Nが入力された場合お釣りを表示して終了
            else:
                MYchange.changedisplay(MYchange.changecalc(balance))
                return
        # 購入できない場合お釣りを表示して終了
        else:
            MYchange.changedisplay(MYchange.changecalc(balance))
            return 
