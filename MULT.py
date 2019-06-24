def digitsProduct(n):
    mult = 1
    for i in n:
        if int(i) != 0:
            mult *= int(i)
    return mult
 
 
x = input('>>>')
print("Произведение значащих цифр:", digitsProduct(x)) 

