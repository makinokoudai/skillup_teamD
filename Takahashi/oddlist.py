name_list = [
    "Kurita", "Tanaka", "Kaneda", "Noda", "Koyama", "Adachi", "Kuriyama", "Ohyama", "Kishida"
]
# 空の奇数の添え字要素のリスト
odd_list =[]
# name_listの要素個数文繰り返す
for i in range(len(name_list)):
    if i % 2 != 0: # iが奇数の場合、name_list[i]をodd_listに追加
        odd_list.append(name_list[i])
    else: # 偶数の場合は処理なし
        continue
# odd_listを出力
print(odd_list,end="")