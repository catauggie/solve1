Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def chet(a):
	if // 2 == 0:
		
SyntaxError: invalid syntax
>>> def chet(a):
	if mod 2 == 0:
		
SyntaxError: invalid syntax
>>> def chet(a):
	if a mod 2 == 0:
		
SyntaxError: invalid syntax
>>> def chet(a):
	if a % 2 == 0:
		print(a, 'четное')
	else:
		print(a, 'нечетное')

		
>>> chet(7)
7 нечетное
>>> chet(456789)
456789 нечетное
>>> def max(a, b):
	if a>b:
		print(a, '>', b)
	elif a<b:
		print(a, '<', b)
	else:
		print(a, '=', b)

		
>>> max(5, 7)
5 < 7
>>> def max2(c, d):
	if c>d:
		print(c, 'max')
	elif c<d:
		print(d, 'max')
	else:
		print('c=d')

		
>>> max2(4, 3)
4 max
>>> max2(5, 5)
c=d
>>> def fu(x)
SyntaxError: invalid syntax
>>> def fu(x):
	if -2.4<=x<=5.7:
		print(x**2)
	else:
		print(4)

		
>>> fu(4)
16
>>> fu(55)
4
>>> def fck_tel(k, t):
	if k==343:
		print(15*t, 'rub')
	elif k==381:
		print(18*t, 'rub')
	elif k==473:
		print(13*t, 'rub')
	elif k==485:
		print(11*t, 'rub')
	else:
		print('fuck up')

		
>>> fck_tel(485, 66)
726 rub
>>> fck_tel(32,2)
fuck up
>>> fck_tel(473, 5454)
70902 rub
>>> def fat(u):
	if u<16:
		print('Выраженный дефицит массы тела - жрать больше надо')
	elif 16<=u<=18.5:
		print('Недостаточная (дефицит) масса тела - харэ быть веганом')
	elif 18,5<=u<=24,99:
		print('Норма - красавчик, ходи в качалку')
	elif 25<=u<=30:
		print('Избыточная масса тела (предожирение) - хватит хавать в макдаке')
	elif 30<=u<=35:
		print('Ожирение - ты просто кусок дерьма')
		
SyntaxError: invalid syntax
>>> def fat(m, h):
	u==m*(h**(-2))
	print(u)
	if u<16:
		print('Выраженный дефицит массы тела - жрать больше надо')
	elif 16<=u<=18.5:
		print('Недостаточная (дефицит) масса тела - харэ быть веганом')
	elif 18.5<=u<=24.99:
		print('Норма - красавчик, ходи в качалку')
	elif 25<=u<=30:
		print('Избыточная масса тела (предожирение) - хватит хавать в макдаке')
	elif 30<=u<=35:
		print('Ожирение - ты просто кусок дерьма')
	elif 35<=u<=40:
		print('Резкое ожирение - у тебя большие проблемы')
	else u>40:
		print('Очень резкое ожирение  - тебе больше ничего не поможет')
		
SyntaxError: invalid syntax
>>> def fat(m, h):
	u==m*(h**(-2))
	print(u)
	if u<16:
		print('Выраженный дефицит массы тела - жрать больше надо')
	elif 16<=u<=18.5:
		print('Недостаточная (дефицит) масса тела - харэ быть веганом')
	elif 18.5<=u<=24.99:
		print('Норма - красавчик, ходи в качалку')
	elif 25<=u<=30:
		print('Избыточная масса тела (предожирение) - хватит хавать в макдаке')
	elif 30<=u<=35:
		print('Ожирение - ты просто кусок дерьма')
	elif 35<=u<=40:
		print('Резкое ожирение - у тебя большие проблемы')
	elif u>40:
		print('Очень резкое ожирение  - тебе больше ничего не поможет')

		
>>> fat(342,55)
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    fat(342,55)
  File "<pyshell#51>", line 2, in fat
    u==m*(h**(-2))
NameError: name 'u' is not defined
>>> m=int(input())
    h=int(input())
    u==m*(h**(-2))
    print(u)
    def fat(u):
	if u<16:
		print(u,'Выраженный дефицит массы тела - жрать больше надо')
	elif 16<=u<=18.5:
		print(u,'Недостаточная (дефицит) масса тела - харэ быть веганом')
	elif 18.5<=u<=24.99:
		print(u,'Норма - красавчик, ходи в качалку')
	elif 25<=u<=30:
		print(u,'Избыточная масса тела (предожирение) - хватит хавать в макдаке')
	elif 30<=u<=35:
		print(u,'Ожирение - ты просто кусок дерьма')
	elif 35<=u<=40:
		print(u,'Резкое ожирение - у тебя большие проблемы')
	elif u>40:
		print(u,'Очень резкое ожирение  - тебе больше ничего не поможет')
		
SyntaxError: multiple statements found while compiling a single statement
>>>     def fat(m, h):
	if m*(h**(-2))<16:
		print(m*(h**(-2)),'Выраженный дефицит массы тела - жрать больше надо')
	elif 16<=m*(h**(-2))<=18.5:
		print(m*(h**(-2)),'Недостаточная (дефицит) масса тела - харэ быть веганом')
	elif 18.5<=m*(h**(-2))<=24.99:
		print(m*(h**(-2)),'Норма - красавчик, ходи в качалку')
	elif 25<=m*(h**(-2))<=30:
		print(m*(h**(-2)),'Избыточная масса тела (предожирение) - хватит хавать в макдаке')
	elif 30<=m*(h**(-2))<=35:
		print(m*(h**(-2)),'Ожирение - ты просто кусок дерьма')
	elif 35<=m*(h**(-2))<=40:
		print(m*(h**(-2)),'Резкое ожирение - у тебя большие проблемы')
	elif m*(h**(-2))>40:
		print(m*(h**(-2)),'Очень резкое ожирение  - тебе больше ничего не поможет')
		
SyntaxError: unexpected indent
>>>  def fat(m, h):
	if m*(h**(-2))<16:
		print(m*(h**(-2)),'Выраженный дефицит массы тела - жрать больше надо')
	elif 16<=m*(h**(-2))<=18.5:
		print(m*(h**(-2)),'Недостаточная (дефицит) масса тела - харэ быть веганом')
	elif 18.5<=m*(h**(-2))<=24.99:
		print(m*(h**(-2)),'Норма - красавчик, ходи в качалку')
	elif 25<=m*(h**(-2))<=30:
		print(m*(h**(-2)),'Избыточная масса тела (предожирение) - хватит хавать в макдаке')
	elif 30<=m*(h**(-2))<=35:
		print(m*(h**(-2)),'Ожирение - ты просто кусок дерьма')
	elif 35<=m*(h**(-2))<=40:
		print(m*(h**(-2)),'Резкое ожирение - у тебя большие проблемы')
	elif m*(h**(-2))>40:
		print(m*(h**(-2)),'Очень резкое ожирение  - тебе больше ничего не поможет')
		
SyntaxError: unexpected indent
>>> 
>>> def fat(m, h):
	if m*(h**(-2))<16:
		print(m*(h**(-2)),'Выраженный дефицит массы тела - жрать больше надо')
	elif 16<=m*(h**(-2))<=18.5:
		print(m*(h**(-2)),'Недостаточная (дефицит) масса тела - харэ быть веганом')
	elif 18.5<=m*(h**(-2))<=24.99:
		print(m*(h**(-2)),'Норма - красавчик, ходи в качалку')
	elif 25<=m*(h**(-2))<=30:
		print(m*(h**(-2)),'Избыточная масса тела (предожирение) - хватит хавать в макдаке')
	elif 30<=m*(h**(-2))<=35:
		print(m*(h**(-2)),'Ожирение - ты просто кусок дерьма')
	elif 35<=m*(h**(-2))<=40:
		print(m*(h**(-2)),'Резкое ожирение - у тебя большие проблемы')
	elif m*(h**(-2))>40:
		print(m*(h**(-2)),'Очень резкое ожирение  - тебе больше ничего не поможет')

>>> 
>>> fat(32,6)
0.8888888888888888 Выраженный дефицит массы тела - жрать больше надо
>>> import rand

