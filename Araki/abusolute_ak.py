#変数に入力された値を代入
import sys
args = sys.argv
num = int(args[1]) 

#abs_numに絶対値を代入
abs_num = abs(num)

#abs_numとnumをstr型に変換して出力
print(str(num) + " " + str(abs_num), end="")