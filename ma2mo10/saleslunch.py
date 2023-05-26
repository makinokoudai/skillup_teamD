import sys

args = sys.argv

chikin_num:int = int(args[1]) # 唐揚げ定食の注文数
curry_num:int = int(args[2])  # カレーセットの注文数

CHIKIN_PRICE:int = 760        # 唐揚げ定食の値段
CURRY_PRICE:int = 850         # カレーセットの値段

# 合計金額を計算
total_sales = (chikin_num * CHIKIN_PRICE) + (curry_num * CURRY_PRICE)
# 売上高を表示
print(total_sales, end="")
