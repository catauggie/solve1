import random
 
 
def set_args():
    return [random.randint(-10, 10) for i in range(10)], random.randint(0, 20)
    
def power(elements, n):
    return -1 if n >= len(elements) else elements[n]**n
    
power(*set_args())
