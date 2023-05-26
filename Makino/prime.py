import sys

#値を入力
input_num = int(sys.argv[1])

#素数かをチェックする関数
def CheckNumber(input_num):
    for i in range(2,input_num):
        if input_num % i == 0:
            return False
    return True

#数字は1000以下で、素数ならprime、それ以外ならnotを出力する
if input_num >= 1000:
    print("1000以上は判定できません", end="")
elif CheckNumber(input_num) and input_num != 1:
        print("prime",end="")
else :
    print("not",end="")
    


    

