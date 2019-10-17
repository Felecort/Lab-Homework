#Напишите функцию, которая выполняет умножение двух числе с 
#использованием только +, -, << (умножение на 2) и >> (деление на 2).

def multiplication(a, b):
#экспериментально установлено, для ускорения работы 
#первое число должно быть меньше второго,
#что и осуществляют следующие 4 строки кода
	if a > b:
		z = a
		a = b
		b = z
	print(a, b)
	bb = b
	num = 0
	c = 1
	while a > c:
		c = c << 1
		num += 1
	c = c >> 1
	num = num - 1
	b = b << num   # b * 2^num
	a -= c 
	while a > 0:
		b += bb
		a -=1
	return b 
def calculator(a, b):
	if a == 0 or b == 0:
		return 0
	elif a > 0 and b > 0:
		return multiplication(a, b)
	elif a < 0 and b < 0:
		a = -a 
		b = -b
		return multiplication(a, b)
	elif a < 0 or b < 0:
		a = abs(a)
		b = abs(b)
		return -multiplication(a, b)



print("результат произведеня =", calculator(-4894564, 54948654))



