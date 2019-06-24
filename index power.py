import random
 
x=int(input())
def set_args():
    return [random.randint(-10, 10) for i in range(x)], random.randint(0, 20)
    
def power(elements, n):
    return -1 if n >= len(elements) else elements[n]**n
    
print(power(*set_args()))
