m = int(input('количество ладей: '))
n = int(input('размер поля: '))
xs = [x for x in range(n)]
ys = [x for x in range(n)]
for i in range(m):
    x = int(input(f'координата x{i}: '))
    y = int(input(f'координата y{i}: '))
    if x in xs:
        xs.remove(x)
    if y in ys:
        ys.remove(y)
print(len(xs) * len(ys))
print(n**2-m)
