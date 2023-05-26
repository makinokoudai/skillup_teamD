import sys
args = sys.argv
# 変数定義
chicken_num = int(args[1])
curry_num = int(args[2])
chicken_fee = 760
curry_fee = 850
# 計算式
amount = chicken_fee * chicken_num + curry_fee * curry_num

print(amount,end="")