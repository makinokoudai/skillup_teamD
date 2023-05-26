#変数に入力された値を代入
import sys
args = sys.argv
fried_chiken_order = int(args[1])
curry_order = int(args[2])

#売上高の計算
earnings = fried_chiken_order * 760 + curry_order * 850
#売上高の出力
print(str(earnings), end="")