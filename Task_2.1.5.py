# готовую библиотечную реализацию квадратного корня использовать 
# nельзя. Напишите функцию, которая вычисляет 
# квадратный корень вещественного числа с помощью поиска.
import math
def Root_Calculation(integer):
	if integer < 0:
		return "число меньше 0"
	degree = 0
	if integer % 1 != 0:
		while integer % 1 > 0:
			integer = integer * 10
			degree += 1
	if degree % 2 != 0:
		degree += 1
		integer *= 10
	degree /= 2
	low = 0
	high = integer // 2
	while low <= high:
		root = (low + (high - low) // 2)
		if root ** 2 == integer:
			return root / (10 ** degree)
		elif root ** 2 < integer:
			low = root + 1
		else:
			high = root - 1
	return root / (10 ** degree)
print(Root_Calculation(458645465.456454646))