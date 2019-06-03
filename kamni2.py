import math
n = int(input())
L = int(input())
R = int(input())
if n>=1 and n<=1000000 and L>=1 and R>=1 and L<=10 and R<=10:
    q=math.trunc(n/(L+R))
    if  L == n:
        print('first')
    if n-q*(L+R)<R:
        print('second')
    else:
        print('first')


