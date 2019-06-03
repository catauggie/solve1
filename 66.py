m = [13, 3, 16, 2, 5, 18]
mas = [m[x] * 10 if  x % 2 else 1 for x in range(len(m))]
print(mas)
