# 必要なモジュールのインポート
import qrcode
import os
import sys
# 引数を入力する
args = sys.argv
file_name = str(args[1])


with open(file_name) as f:
    i = 1
    for line in f:
        path = os.path.join(".","output",f"{i}.png")
        img = qrcode.make(line)
        img.save(path)
        i = i + 1
