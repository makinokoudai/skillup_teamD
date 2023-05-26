from decimal import Decimal, ROUND_HALF_UP
import sys
args = sys.argv

karaage = int(args[1])
curry = int(args[2])

sales = karaage * 760 + curry * 850
sales_kareage = karaage * 760
prime_karaage = sales_kareage * 0.323
sales_curry = curry* 850
prime_curry = sales_curry * 0.284

prime = prime_karaage + prime_curry
demi_prime = Decimal(prime).quantize(Decimal('0'), rounding=ROUND_HALF_UP)
gross_profit = sales - demi_prime

print("売上高："+str(sales)+"、原価："+str(demi_prime)+"、粗利："+str(gross_profit),end="")