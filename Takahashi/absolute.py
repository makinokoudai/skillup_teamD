import sys
args = sys.argv

num = int(args[1])
if num < 0:
    absolute = num * (-1) 
else:
    absolute = num

print(str(num)+" "+str(absolute),end="")