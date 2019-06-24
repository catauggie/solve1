Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> "У лукоморья 123 дуб зеленый 456".len()
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    "У лукоморья 123 дуб зеленый 456".len()
AttributeError: 'str' object has no attribute 'len'
>>> "У лукоморья 123 дуб зеленый 456".count()
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    "У лукоморья 123 дуб зеленый 456".count()
TypeError: count() takes at least 1 argument (0 given)
>>> len("У лукоморья 123 дуб зеленый 456")
31
>>> if len("У лукоморья 123 дуб зеленый 456")>4:
	print("У лукоморья 123 дуб зеленый 456".lower())

	
у лукоморья 123 дуб зеленый 456
>>> s="У лукоморья 123 дуб зеленый 456"
>>> 'О' + s[1:]
'О лукоморья 123 дуб зеленый 456'
>>> import sys
>>> sys.path
['', 'C:\\Users\\ivan\\AppData\\Local\\Programs\\Python\\Python37-32\\Lib\\idlelib', 'C:\\Users\\ivan\\AppData\\Local\\Programs\\Python\\Python37-32\\python37.zip', 'C:\\Users\\ivan\\AppData\\Local\\Programs\\Python\\Python37-32\\DLLs', 'C:\\Users\\ivan\\AppData\\Local\\Programs\\Python\\Python37-32\\lib', 'C:\\Users\\ivan\\AppData\\Local\\Programs\\Python\\Python37-32', 'C:\\Users\\ivan\\AppData\\Local\\Programs\\Python\\Python37-32\\lib\\site-packages']
>>> import stroka
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    import stroka
  File "C:\Users\ivan\AppData\Local\Programs\Python\Python37-32\Lib\idlelib\stroka.py", line 3
    print(s.upper())
                   ^
TabError: inconsistent use of tabs and spaces in indentation
>>> h=['Hi', 27 , -8.1, [1,2]]
>>> h[1]='hello'
>>> h
['Hi', 'hello', -8.1, [1, 2]]
>>> h=['bonjour','привет','hola','aloha','привіт']
>>> h[1]='hello'
>>> h
['bonjour', 'hello', 'hola', 'aloha', 'привіт']
>>> max(h)
'привіт'
>>> min(h)
'aloha'
>>> sorted(h)
['aloha', 'bonjour', 'hello', 'hola', 'привіт']
>>> sum(h)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    sum(h)
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> len(h)
5
>>> L = [3, 6, 7, 4, -5, 4, 3, -1]
>>> if sum(L)>2:
	print(len(L))

	
8
>>> if abs(max(L)-min(L))<10:
	print(sorted(L))
    else:
	    
SyntaxError: unindent does not match any outer indentation level
>>> if abs(max(L)-min(L))<10:
	print(sorted(L))
	else:
		
SyntaxError: invalid syntax
>>> if abs(max(L)-min(L))>10:
	print(sorted(L))
else:
	print('разность меньше 10')

	
[-5, -1, 3, 3, 4, 4, 6, 7]
>>> original=['H','B']
>>> final=original+['T']
>>> final
['H', 'B', 'T']
>>> final=final*5
>>> final
['H', 'B', 'T', 'H', 'B', 'T', 'H', 'B', 'T', 'H', 'B', 'T', 'H', 'B', 'T']
>>> final=final/5
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    final=final/5
TypeError: unsupported operand type(s) for /: 'list' and 'int'
>>> del final[0]
>>> final
['B', 'T', 'H', 'B', 'T', 'H', 'B', 'T', 'H', 'B', 'T', 'H', 'B', 'T']
>>> def f(x,y):
return x+y
SyntaxError: expected an indented block
>>> def f(x,y):
	return x+y

>>> f([1,2,3],[4,5,6])
[1, 2, 3, 4, 5, 6]
>>> f("123", "456")
'123456'
>>> f(1,2)
3
>>> =['bonjour',7,'hola',-1.0,'привіт']
SyntaxError: invalid syntax
>>> h=['bonjour',7,'hola',-1.0,'привіт']
>>> if 7 in h:
print ('Значение есть в списке')
SyntaxError: expected an indented block
>>> if 7 in h:
	print ('Значение есть в списке')

	
Значение есть в списке
>>> L = [3, 'hello', 7, 4, 'привет', 4, 3, -1]
>>> if 'привет' in L:
	print (10*'Значение есть в списке')

	
Значение есть в спискеЗначение есть в спискеЗначение есть в спискеЗначение есть в спискеЗначение есть в спискеЗначение есть в спискеЗначение есть в спискеЗначение есть в спискеЗначение есть в спискеЗначение есть в списке
>>> if 'привет' in L:
	print (10*'\nЗначение есть в списке')

	

Значение есть в списке
Значение есть в списке
Значение есть в списке
Значение есть в списке
Значение есть в списке
Значение есть в списке
Значение есть в списке
Значение есть в списке
Значение есть в списке
Значение есть в списке
>>> h=['bonjour',7,'hola',-1.0,'привіт']
>>> h
['bonjour', 7, 'hola', -1.0, 'привіт']
>>> g=h[1:2]
>>> g
[7]
>>> a = [-1, 1, 66.25, 333, 333, 1234.5]
>>> del a[0]
>>> a
[1, 66.25, 333, 333, 1234.5]
>>> del a[2:5}
SyntaxError: invalid syntax
>>> del a[2:5]
>>> a
[1, 66.25]
>>> del[:]
SyntaxError: invalid syntax
>>> a
[1, 66.25]
>>> h
['bonjour', 7, 'hola', -1.0, 'привіт']
>>> p=h
>>> p
['bonjour', 7, 'hola', -1.0, 'привіт']
>>> p[0]=1
>>> h
[1, 7, 'hola', -1.0, 'привіт']
>>> p
[1, 7, 'hola', -1.0, 'привіт']
>>> x=y=[1,2]
>>> x is y
True
\
>>> x=[d,sd]
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    x=[d,sd]
NameError: name 'd' is not defined
>>> x=2,3]
SyntaxError: invalid syntax
>>> x=[2,3]
>>> y=[6,7]
>>> x is y
False
>>> y is x
False
>>> a = [4, 3, [2, 1]]
>>> b=a[:]
>>> b is a
False
>>> b[2][0]=-100
>>> a
[4, 3, [-100, 1]]
>>> import copy
>>> b = copy.deepcopy(a)
>>> b[2][0]=-100
>>> a
[4, 3, [-100, 1]]
>>> L = [3, 'hello', 7, 4, 'привет', 4, 3, -1]
>>> L[:3]
[3, 'hello', 7]
>>> L[:]
[3, 'hello', 7, 4, 'привет', 4, 3, -1]
>>> L[::2]
[3, 7, 'привет', 3]
>>> L[::-1]
[-1, 3, 4, 'привет', 4, 7, 'hello', 3]
>>> L[:-1]
[3, 'hello', 7, 4, 'привет', 4, 3]
>>> L[-1:]
[-1]
>>> colors=['red', 'orange', 'green']
>>> colors.extend(['black','blue'])
>>> colors
['red', 'orange', 'green', 'black', 'blue']
>>> colors.append('purple')
>>> colors
['red', 'orange', 'green', 'black', 'blue', 'purple']
>>> colors.insert(2,'yellow')
>>> colors
['red', 'orange', 'yellow', 'green', 'black', 'blue', 'purple']
>>> colors.remove('black')
>>> colors
['red', 'orange', 'yellow', 'green', 'blue', 'purple']
>>> colors.count('red')
1
>>> colors.index('green')
3
>>> colors
['red', 'orange', 'yellow', 'green', 'blue', 'purple']
>>> colors.pop()
'purple'
>>> colors
['red', 'orange', 'yellow', 'green', 'blue']
>>> colors.reverse()
>>> colors
['blue', 'green', 'yellow', 'orange', 'red']
>>> colors.sort()
>>> colors
['blue', 'green', 'orange', 'red', 'yellow']
>>> colors.clear()
>>> colors
[]
>>> s='Строка для изменения'
>>> list(s)
['С', 'т', 'р', 'о', 'к', 'а', ' ', 'д', 'л', 'я', ' ', 'и', 'з', 'м', 'е', 'н', 'е', 'н', 'и', 'я']
>>> lst = list(s)
>>> lst
['С', 'т', 'р', 'о', 'к', 'а', ' ', 'д', 'л', 'я', ' ', 'и', 'з', 'м', 'е', 'н', 'е', 'н', 'и', 'я']
>>> lst[0]='э'
>>> lst
['э', 'т', 'р', 'о', 'к', 'а', ' ', 'д', 'л', 'я', ' ', 'и', 'з', 'м', 'е', 'н', 'е', 'н', 'и', 'я']
>>> s=''.join(lst)
>>> s
'этрока для изменения'
>>> A = ['red', 'green', 'blue']
>>> ' '.join(A)
'red green blue'
>>> ' '.join(A)
'red green blue'
>>> 'G'.join(A)
'redGgreenGblue'
>>> ' pnx'.join(A)
'red pnxgreen pnxblue'
>>> A
['red', 'green', 'blue']
>>> n=73485384753846538465
>>> lict(n)
Traceback (most recent call last):
  File "<pyshell#136>", line 1, in <module>
    lict(n)
NameError: name 'lict' is not defined

>>> list(n)
Traceback (most recent call last):
  File "<pyshell#137>", line 1, in <module>
    list(n)
TypeError: 'int' object is not iterable
>>> list(str(n))
['7', '3', '4', '8', '5', '3', '8', '4', '7', '5', '3', '8', '4', '6', '5', '3', '8', '4', '6', '5']
>>> for i in list(str(n)):
	print(count(n))

	
Traceback (most recent call last):
  File "<pyshell#160>", line 2, in <module>
    print(count(n))
NameError: name 'count' is not defined
>>> s='d a dd dd gg rr tt yy rr ee'.split()
>>> s
['d', 'a', 'dd', 'dd', 'gg', 'rr', 'tt', 'yy', 'rr', 'ee']
>>> s='d:a:dd:dd:gg:rr:tt:yy:rr:ee'.split(":")
>>> s
['d', 'a', 'dd', 'dd', 'gg', 'rr', 'tt', 'yy', 'rr', 'ee']
>>> s='d:a:dd:dd:gg:rr:tt:yy:rr:ee'.split("d")
>>> s
['', ':a:', '', ':', '', ':gg:rr:tt:yy:rr:ee']
>>> s='d:a:dd:dd:gg:rr:tt:yy:rr:ee'.split("d, g")
>>> s
['d:a:dd:dd:gg:rr:tt:yy:rr:ee']
>>> s='d:a:dd:dd:gg:rr:tt:yy:rr:ee'.split("d", "g")
Traceback (most recent call last):
  File "<pyshell#169>", line 1, in <module>
    s='d:a:dd:dd:gg:rr:tt:yy:rr:ee'.split("d", "g")
TypeError: 'str' object cannot be interpreted as an integer
>>> L = [3, 'hello', 7, 4, 'привет', 4, 3, -1]
>>> if 'привет' in L:
	print (del('привет'))
	
SyntaxError: invalid syntax
>>> if 'привет' in L:
	print(L.remove('привет'))

	
None
>>> L.count(4)
2
>>> if L.count(4)>1:
	print(L.clear())

	
None
>>> lst=[['A', 1], ['B',2], ['C',3]]
>>> lst
[['A', 1], ['B', 2], ['C', 3]]
>>> lst[0][1]
1
>>> lst[2][1]
3
>>> 
