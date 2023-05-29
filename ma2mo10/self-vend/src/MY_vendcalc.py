import MY_display_item as MYdisp
import MY_buy_drink as MYbuy

def main():
    # 商品リストを表示
    MYdisp.display_item()
    # 投入金額と商品名の入力を受け取る
    money, item_name = MYdisp.set_item()

    # item_nameが空ならcancelされたので終了
    if item_name == []:
        return 
    
    MYbuy






if __name__ == "__main__":
    main()