import sys

fried_hicken_number = int(sys.argv[1]) 
curry_number = int(sys.argv[2]) 

#唐揚げ定食の値段
fried_hicken_fee = 760

#カレーセットの値段
curry_fee = 850

# 売り上げ計算
def sum(fried_hicken_number,curry_number):
    sum_day = fried_hicken_number * fried_hicken_fee + curry_number * curry_fee
    print(sum_day,end="")
    

# 結果を出力
sum(fried_hicken_number,curry_number)
    
    