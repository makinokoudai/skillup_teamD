
#絶対値と引数を表示する問題

import sys

#値を入力
input_number = int(sys.argv[1])

#値を絶対値に変換
abs_number = abs(input_number)

#結果を出力
print(f"{input_number} {abs_number}",end="")