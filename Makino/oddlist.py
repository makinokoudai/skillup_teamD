

#データの入力
text = ["Kurita","Tanaka","Kaneda","Noda","Koyama","Adachi","Kuriyama","Ohyama","Kishida"]

output_name =[]

#カウントする変数
count = 0

#リストから名前を取ってきて、添え字が奇数のみ出力
for name in text:
    if count % 2 != 0:
        output_name.append(name)
    count += 1



print(output_name,end="")
        
        

