import qrcode
import os
import sys
args = sys.argv

# 引数を変数fileに代入
file = args[1]
# 変数count（txtファイルの行数をカウント）の初期化
count = 0

# qrコード作成
with open(file, "r", encoding="utf-8") as f: # 読み込みモードでファイルを開く
    for line in f: # 一行ずつ読み込み
        count += 1 # 行数カウント
        img = qrcode.make(line) # qrコード作成
        path = os.path.join("..", "..", "output",str(count)+".png") # パスの作成
        img.save(path) # 作成したパスでqrコードを保存

