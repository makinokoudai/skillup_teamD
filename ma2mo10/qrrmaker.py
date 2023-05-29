import os
import qrcode
import sys

args = sys.argv

filename:str = args[1]
cnt:int = 1

with open(filename) as f:
    lines = f.readlines()
    for line in lines:
        #QRコードを生成する
        img = qrcode.make(line)
        #画像を保存
        img.save(f'../../output/{cnt}.png')
        cnt += 1
