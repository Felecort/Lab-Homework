#Напишите функцию, которая выполняет умножение двух числе с 
#использованием только +, -, << (умножение на 2) и >> (деление на 2).
def multiplication(a, b):
	bb = b
	num = 0
	c = 1
	while a > c:
		c = c << 1
		num += 1
	c = c >> 1
	num = num - 1
	b = b << num # b * 2^num
	a -= c 
	while a > 0:
		b += bb
		a -=1
	return b 

a = 3472299622
b = -564155
if a == 0 or b == 0:
	print("результат произведения = 0")
elif a < 0 or b < 0:
	t = -1
	a = abs(a)
	b = abs(b)
	bb = b
	if a < b:
		q = multiplication(a,b)
		print("результат произведения =", q-q-q)
	else:
		z = a
		a = b
		b = z
		q = multiplication(a,b)
		print("результат произведения =", q-q-q) 
else:
	if a < b:
		print("результат произведения =",multiplication(a, b))
	else:
		z = a
		a = b
		b = z
		print("результат произведения =",multiplication(a, b))
