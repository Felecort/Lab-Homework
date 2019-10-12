# готовую библиотечную реализацию квадратного корня использовать 
# nельзя. Напишите функцию, которая вычисляет 
# квадратный корень вещественного числа с помощью поиска.



def fraction(number):
    s = str(number)
    if '.' in s:
        return abs(s.find('.') - len(s)) - 1
    else:
        return 0
def sqrt(a_power_10, a, num):
	squares = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
	for j in range(round(len(str(a))/2)):
		a_count = a_power_10 // 10**(num + 1)
		for i in range(10):
			if a_count > squares[i-1] and a_count < squares[i]:
				print(a_count, "   ", i) 
		num = num - 1


a = 3743.215610
num = fraction(a)
sqrt(a * 10**num, a, num)
