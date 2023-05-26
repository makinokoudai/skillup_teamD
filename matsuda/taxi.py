import sys
args = sys.argv
# 変数定義
distance = int(args[1])
first_distance = 1500
first_fee = 630
add_fee = 98
add_distance = 344

if distance > first_distance:
    i = (distance - first_distance)//add_distance + 1 # ＋1は切り上げをするため
    pay = i * add_fee + first_fee

else:
    pay = first_fee

print(pay,end="")
