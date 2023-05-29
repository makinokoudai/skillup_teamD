# メインモジュール
from vend_module import MY_display_item as MYdisp
from vend_module import MY_buy_drink as MYbuy

def main():
    # 商品リストを表示
    MYdisp.display_item()
    # 投入金額と商品名の入力を受け取る
    money, item_name = MYdisp.set_item()

    # item_nameが空ならcancelされたので終了、それ以外なら購入
    if item_name == '':
        return
    else:
        MYbuy.buy_drink(item_name, money)






if __name__ == "__main__":
    main()