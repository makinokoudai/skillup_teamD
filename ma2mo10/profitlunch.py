import sys
from decimal import Decimal, ROUND_HALF_UP

args = sys.argv

chikin_num:int = int(args[1]) # 唐揚げ定食の注文数
curry_num:int = int(args[2])  # カレーセットの注文数

CHIKIN_PRICE:int = 760        # 唐揚げ定食の値段
CURRY_PRICE:int = 850         # カレーセットの値段

CHIKIN_RATE:float = 0.323
CURRY_RATE:float = 0.284


chikin_sales = chikin_num * CHIKIN_PRICE
curry_sales = curry_num * CURRY_PRICE
# 合計金額を計算
total_sales = chikin_sales + curry_sales

total_cost = Decimal(str(chikin_sales * CHIKIN_RATE)).quantize(Decimal('0'), rounding=ROUND_HALF_UP) + Decimal(str(curry_sales * CURRY_RATE)).quantize(Decimal('0'), rounding=ROUND_HALF_UP)

print(f"売上高：{total_sales}、原価：{total_cost}、 粗利：{total_sales - total_cost}", end="")