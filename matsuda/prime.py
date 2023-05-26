import sys
args = sys.argv
input1 = int(args[1])
if input1 >= 1000:
    print("1000以上は判定できません",end="")
elif input1 == 1:
    print("prime",end="")
else:
    for i in range(2,input1-1):
        if input1 % i == 0:
            txt = "not"
            break
        else:
            txt = "prime"
    print(txt,end="")
    
