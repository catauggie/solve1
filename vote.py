n = int(input())
s = []
my_friends = range(n)
for i in my_friends:
    a,b,c = map(int,input().split())
    if a < b and c == 0:
        s.append(1)
    if a < b and c > 0:
        s.append(1 + c)
    else:
        s.append(0)
print(sum(s))
