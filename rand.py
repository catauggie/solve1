import random
a = random.randint(0, 10)
def rand(a, n):
    if a==n:
        print('win')
    else:
        print('repeat')
n=int(input('введите число'))
print(a, '-загадано')
print(rand(a,n))

