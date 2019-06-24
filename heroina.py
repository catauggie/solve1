def heroina(a, b, c):
    return ((a+b+c)/2*((a+b+c)/2-a)*((a+b+c)/2-b)*((a+b+c)/2-c))**(1/2)

a=int(input("Введите значение: "))
b=int(input("Введите значение: "))
c=int(input("Введите значение: "))
print(heroina(a, b, c))
