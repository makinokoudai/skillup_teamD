import sys
args = sys.argv
# 変数定義
chicken_num = int(args[1])
curry_num = int(args[2])
chicken_fee = 760
curry_fee = 850
chicken_rate = 0.323
curry_rate = 0.284

# 計算式
sales = chicken_fee * chicken_num + curry_fee * curry_num
cost = round((chicken_fee * chicken_num) * chicken_rate) + round((curry_fee * curry_num) * curry_rate)
profit = sales - cost
print("売上高：{0}、原価：{1}、粗利：{2}".format(sales,cost,profit),end="")
