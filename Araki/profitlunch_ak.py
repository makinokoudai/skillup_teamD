#変数に入力された値を代入
from decimal import Decimal, ROUND_HALF_UP
import sys
args = sys.argv
fried_chiken_order = int(args[1]) 
curry_order = int(args[2])

#単価、原価率、売上個数から総原価と総粗利を算出する関数
def calc_cost(price,cost_rate,amount):
    price *= amount
    cost = price * cost_rate //100
    #四捨五入
    cost = Decimal(cost).quantize(Decimal('0'), rounding=ROUND_HALF_UP)
    profit = price - cost
    return cost , profit

#商品ごとの総原価と総粗利を変数に代入
fr_ch_cost, fr_ch_profit = calc_cost(760,32.3,fried_chiken_order)
curry_cost, curry_profit = calc_cost(850,28.4,curry_order)

#原価と粗利を合算し、表示数値を算出
total_cost = fr_ch_cost + curry_cost
total_profit = fr_ch_profit + curry_profit
total_earnings = str(total_cost + total_profit)

#合算した売上高と原価、粗利を表示
print("売上高：" + total_earnings + 
      "、原価：" + str(total_cost) + 
      "、粗利：" + str(total_profit))