#変数に入力された値を代入
import sys
args = sys.argv
dist = int(args[1])

#距離が1500より多い場合
if dist > 1500:
    dist = dist  - 1500
    #1500mを引いた距離で整数解を出して金額計算
    taxi_fare = 630 + 98 * (dist // 344 + 1)
    print(str(taxi_fare), end="")

#距離が1500より少ない場合
else:
    print("630", end="")
