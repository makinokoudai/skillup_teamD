import sys 
args = sys.argv
# 引数を変数numに代入
num = int(args[1])
# 素数判定
if num >= 1000: # 1000以上が入力された場合
    print("1000以上は判定できません",end="")
elif num < 1: # 0、負の値が入力された場合 
    print("not",end="")
else: # 素数ではない場合
    for i in range(2, num-1):
        if num % i == 0:
            print("not",end="")
            break
    else: # 素数の場合
        print("prime",end="")


