a = str(input())
n = int(input())
x = str(input())
for i in a:
     if i == x:
         break
    # else:
    #     print('Буквы' 'x' 'в строке нет')
     else:
         print(i*n, end='')
