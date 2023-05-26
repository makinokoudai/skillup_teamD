#名前の格納配列と奇数の添え字を格納する配列を定義
names = ["Kurita", "Tanaka", "Kaneda", "Noda", "Koyama", 
         "Adachi", "Kuriyama", "Ohyama", "Kishida"]
odd_list =[]

#i=1からnamesの要素数分2ずつ加算されるfor文
for i in range(1,len(names),2):
    odd_list.append(names[i])

#リストにした名前を出力
print(odd_list,end="")