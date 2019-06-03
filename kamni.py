import random
import math
n = int(input('количество камней в куче: '))
k = int(input('количество камней, взятое 1-ым игроком: '))
stones_1 = range(k)
for i in stones_1:
    print(random.randint(1, 10))
m = int(input('количество камней, взятое 2-ым игроком: '))
stones_2 = range(m)
for i in stones_2:
    print(random.randint(1, 10))
q=math.trunc(n/(m+k))
if  k == n:
    print('first')
if n-q*(m+k)<m:
    print('second')
else:
    print('first')

