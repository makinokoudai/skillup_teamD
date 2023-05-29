from decimal import Decimal, ROUND_HALF_UP
import sys
args = sys.argv
# 引数を変数karaage,curryにそれぞれ代入
karaage = int(args[1])
curry = int(args[2])

# 唐揚げ、カレーそれぞれの売り上げを計算
sales_kareage = karaage * 760
sales_curry = curry* 850
# 唐揚げ、カレーそれぞれの原価を計算
prime_karaage = sales_kareage * 0.323
prime_curry = sales_curry * 0.284
# 総売上を計算
sales = karaage * 760 + curry * 850
# 唐揚げ、カレーの原価の合計
prime = prime_karaage + prime_curry
# 原価の少数第一位を四捨五入
demi_prime = Decimal(prime).quantize(Decimal('0'), rounding=ROUND_HALF_UP)
# 粗利の計算
gross_profit = sales - demi_prime
# 出力
print("売上高："+str(sales)+"、原価："+str(demi_prime)+"、粗利："+str(gross_profit),end="")