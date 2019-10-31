# готовую библиотечную реализацию квадратного корня использовать 
# nельзя. Напишите функцию, которая вычисляет 
# квадратный корень вещественного числа с помощью поиска.
def calculator(a):
	#проверка, являчется ли число положительным 
	assert a >= 0
	#определение количества знаков после запятой
	s = str(a)
	if '.' in s:
	    length =  abs(s.find('.') - len(s)) - 1
	else: 
		length = 0 
	if length % 2 != 0:
		length += 1
	#перевод вещественного числа в натуральное
	a10 = a * (10 ** length)
	a10 = int(a10)
	#вычисление корня с помощью поиска
	j = 0
	sqrt = 0
	while j != 1:
		if (sqrt * sqrt)<= a10 and ((sqrt + 1) * (sqrt + 1)) > a10:
			j = 1
		else: sqrt += 1
	sqrt = sqrt / ((10 ** (length / 2)))
	return sqrt

print(calculator(5000000))
print(calculator(455.1554))
print(calculator(56496))
print(calculator(56444.564879))
print(calculator(123.5164889))