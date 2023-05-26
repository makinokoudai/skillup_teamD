import sys
args = sys.argv
# 引数入力
num = int(args[1])
# 絶対値判別
if num < 0:
    absolute = num * -1
else:
    absolute = num    

print(num,absolute,end="")