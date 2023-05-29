import sys
args = sys.argv
input1 = int(args[1])
if input1 >= 1000: # 1000以上の処理
    print("1000以上は判定できません",end="")
elif input1 == 1: # セミナーアシストに対応させるために1のときの処理
    print("prime",end="")
else: # 素数以外の処理
    for i in range(2,input1-1):
        if input1 % i == 0:
            txt = "not"
            break
        else: # 素数の時の処理
            txt = "prime"
    print(txt,end="")
    
