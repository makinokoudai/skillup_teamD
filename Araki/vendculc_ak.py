#商品と金額を格納した辞書型
list_price = {"お茶": 110, "コーヒー": 100, "ソーダ": 160, "コーンポタージュ": 130}

#商品名と金額を一覧にして表示
for name, price in list_price.items():
    print(name + "：" + str(price) + "円")

#投入金額の整合性確認
def check_money(money):
    money_flag = False
    while money_flag == False:
        money = int(input("投入金額を入力してください "))
        if money > 10000:
            print("10,000円を超える金額は投入できません。再度投入金額を入力してください")
        elif money % 10 != 0:
            print("1円玉、5円玉は使用できません。再度投入金額を入力してください")
        elif min(list_price.values()):
            print(money + "円では購入できる商品がありません。再度投入金額を入力してください")
        else:
            money_flag = True
            return money

#おつりの計算
def change_money(money):
    #おつり用リスト
    moneys = {"5000円札": 0, "1000円札": 0, "500円玉": 0,
                "100円玉": 0, "50円玉": 0, "10円玉": 0}
    while money != 0:
        if money >= 5000:
            moneys["5000円札"] += 1
            money -= 5000
        elif money >= 1000:
            moneys["1000円札"] += 1
            money -= 1000
        elif money >= 500:
            moneys["500円玉"] += 1
            money -= 500
        elif money >= 100:
            moneys["100円玉"] += 1
            money -= 100
        elif money >= 50:
            moneys["50円玉"] += 1
            money -= 50
        elif money >= 10:
            moneys["10円玉"] += 1
            money -= 10
    #枚数格納用リスト
    result_moneys = {}
    for i, v in moneys.items():
        if v != 0:
            result_moneys[i] = v
    return result_moneys

#おつりの表示
def print_moneys(moneys):
    print("おつり")
    for i, v in moneys.items():
        print( i +"：" + v +"枚")

#商品の購入
def buy_product(money):
    action = input("何を購入しますか（商品名/cancel）")
    if action == "cancel":
        print_moneys(change_money(money))
        exit()
    money -= list_price[action]
    return money

#関数の呼び出し
money = check_money()
money = buy_product(money)

#購入用ループ
while money >= min(list_price.values()):
    print("残金：" + money)
    check = input("続けて購入しますか？（Y/N）")
    #Yの場合
    if check == "Y":
        for i, v in list_price.items():
            print( i +"：" + v +"枚")
        money = buy_product(money)
    #Nの場合
    elif check == "N":
        print_moneys(change_money(money))
        exit()
else:
    print_moneys(change_money(money))

