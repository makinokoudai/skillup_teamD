#変数に入力された値を代入
import sys
args = sys.argv
num = int(args[1]) 

#素数判定
if num >= 1000: #1000以上の場合
    print("1000以上は判定できません",end="")
else: #1000以下の場合
    for i in range(2, int(num**0.5) + 1): #numの√2までfor文を回す
        if num % i == 0: #割り切れた場合、notと出力して抜ける
            print("not",end="")
            break
    else: #一度もヒットしなかった場合素数と出力
        print("prime",end="")