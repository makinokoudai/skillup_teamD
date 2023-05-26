
#タクシー運賃を計算する

import sys

#値を入力
input_number = int(sys.argv[1])

#合計金額
sum = 0

#初乗り料金
first_fee = 630


# corrent_distance= 0

if input_number <= 1500 :
    print(first_fee,end="")
else :
    input_number -= 1500
    
    #344mごとが何回あるか確認　
    count_distance = input_number // 344 + 1 
    
    sum = first_fee + count_distance * 98 
    
    print(sum,end="")
        
