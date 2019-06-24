def find_message(s):
    result = ""
    for i in s:
        if i.isupper():
            result += i
    return result
 
 
a = input('>>> ')
print(find_message(a))
