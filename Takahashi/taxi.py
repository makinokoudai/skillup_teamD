import sys
import math
args = sys.argv


distance = int(args[1])

# 運賃算出
if distance <= 1500:
    fare = 630
elif 0 < distance - 1500 < 1:
    fare = 98 + 630
else:
    add_distance = distance - 1500
    add_fare = add_distance // 344
    fare = (add_fare + 1) * 98 + 630

print(fare,end="")