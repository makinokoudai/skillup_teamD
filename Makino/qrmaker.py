import os
import qrcode
import sys

args = sys.argv

# ファイル名の入力
input_file_name = str(sys.argv[1])

# ファイルのパス
file_path = f"../../output/{input_file_name}"

# カウント変数
count = 1  



                
# ファイルを開いてQRコードを作成
with open(file_path) as f:
    # URLを一行ずつ読み込み
    read_line = f.readlines()
    
    for line in read_line:
    
        img = qrcode.make(line)
        
        #　画像を保存する
        img.save(f"../../output/{str(count)}.png")
        count += 1