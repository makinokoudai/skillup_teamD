import qrcode
import os
import sys
args = sys.argv

#入力されたパスのファイルを開く
with open(str(args[1])) as f:
    filename = 1
    #各行ごとに QRコードにして保存
    for line in f:
        path = os.path.join("files",str(filename) + ".png")
        img = qrcode.make(line)
        img.save(path)
        filename += 1
