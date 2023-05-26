import sys
from decimal import *

#それぞれの販売個数を入力
fried_hicken_number = int(sys.argv[1]) 
curry_number = int(sys.argv[2]) 


#唐揚げ定食の値段
fried_hicken_fee = 760

#唐揚げ定食の原価率
fried_hicken_rate = 0.323 

#カレーセットの値段
curry_fee = 850

#カレーげ定食の原価率
curry_rate = 0.284 


#売上高の初期化
sum = 0

#原価の初期化
cost_price = 0

#粗利の初期化
gross_profit = 0


def calc(fried_hicken_number,curry_number ):
    fried_hicken_sales = fried_hicken_fee * fried_hicken_number
    curry_sales = curry_fee * curry_number
    
    # 全売り上げを計算
    sum = fried_hicken_sales + curry_sales
    
    #原価
    fried_hicken_cost = fried_hicken_sales * fried_hicken_rate
    curry_cost = curry_sales * curry_rate
    
    #全原価を算出
    cost_price = Decimal(fried_hicken_cost + curry_cost).quantize(Decimal('0'), rounding=ROUND_HALF_UP)
    
    #粗利の算出
    gross_profit = sum - int(cost_price)
    
    print(f"売上高：{sum}、原価：{cost_price}、粗利：{gross_profit}", end="")



    
calc(fried_hicken_number,curry_number )
    
    


    
    
    
    

