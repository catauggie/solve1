import math
def sinus(x):
    return (1-(math.sin(x))**2)**(1/2)
x=float(input("Введите значение: "))
print(sinus(x))
