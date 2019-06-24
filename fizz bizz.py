def checkio(n):
    if n%5==0:
        return "Buzz"
    if n%3==0:
        return "Fizz"
    if n%5==0 and n%3==0:
        return "Fizz Buzz"
    else:
        return str(n)
n=int(input())        
print(checkio(n))
