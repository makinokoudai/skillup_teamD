import os
import qrcode
import sys

args = sys.argv

filename:str = args[1]       # ファイル名
cnt:int = 1                  # カウント変数

# ファイルを開く
with open(filename) as f:
    # 1行ずつ読み込む
    lines = f.readlines()
    for line in lines:
        #QRコードを生成する
        img = qrcode.make(line)
        #画像を保存
        img.save(f'../../output/{cnt}.png')
        cnt += 1
