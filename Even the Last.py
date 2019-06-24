def checkio(arr):
    summ = 0
    if 0<len(arr)<20:
        for i in range(len(arr)):
            if not i % 2:
                summ += arr[i]
        return summ * arr[-1]
    else:
        return 0
 
 
print(checkio(range(int(input('>>> ')))))

