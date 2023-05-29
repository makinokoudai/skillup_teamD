# メインモジュール
import display_item_db as dispDB
from vend_module import MY_input as MYin
from vend_module import MY_buy_drink as MYbuy

def main():
    # 商品リストを表示
    dispDB.display_item_db()
    #金額の入力を受け付ける
    money = MYin.input_money()
    #商品名/cancelの入力を受け付ける
    item_name = MYin.input_item(money)

    # item_nameが空ならcancelされたので終了、それ以外なら購入
    if item_name == '':
        return
    else:
        MYbuy.buy_drink(item_name, money)






if __name__ == "__main__":
    main()