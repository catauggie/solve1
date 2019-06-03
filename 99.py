mas = []
n = int(input())
for i in range(n):
    mas.append(i)
only_3 = list(filter(lambda x: x == i**2, mas))
print(only_3)
