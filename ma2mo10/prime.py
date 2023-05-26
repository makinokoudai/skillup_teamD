import sys

args = sys.argv

num = int(args[1])
    

def prime_judge(num:int) -> bool:
    # 2からN-1まで割り切れるか判定
    for i in range(2, num):
        if num % i == 0:
            return False
        
    return True
# 1000以上の場合
if num >= 1000:
    print("1000以上は判定できません", end="")
# 素数なら"Prime"をそれ以外なら"not"を表示
elif prime_judge(num)  and num != 1:
    print("Prime", end="")
else:
    print("not", end="")