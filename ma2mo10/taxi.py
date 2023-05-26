import sys

args = sys.argv


distance:int = int(args[1]) # 距離
fare:int = 630              # 運賃

# 距離が1500m以上なら344mごとに98円運賃に加算
if distance > 1500:
    distance -= 1500
    fare += 98
    while distance >= 344:
        distance -= 344
        fare += 98
    
# 運賃を表示
print(fare, end="")
