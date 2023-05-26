from typing import List

name_list:List[str] = ["Kurita", "Tanaka", "Kaneda", "Noda", "Koyama", "Adachi", "Kuriyama", "Ohyama", "Kishida"]
oddlist:List[str] = []

for i in range(0, len(name_list)):
    if i % 2 != 0:
        oddlist.append(name_list[i]) 
    
print(oddlist, end="")