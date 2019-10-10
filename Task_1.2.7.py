import time
a = int(input("ввeдите число "))
numbers = {}
lst = []
b = []

#таймер выполнения кода 
start_time = time.time()

#-------------------------------------------

def decomposition(n):
	c = 1
	l = 0
	f = 1
	while f <= a:
		f = n ** c
		l = l + a // f
		c += 1
	numbers[n] = l

#-------------------------------------------

#Решето Эратосфена
for n in range(a+1):
	b.append(n)		
i = 2				
while i <= a:		
    if b[i] != 0:	
        lst.append(b[i])
        for j in range(i, a+1, i):
            b[j] = 0
    i += 1
#-------------------------------------------
for element in lst:
	n = element
	decomposition(n)
print(numbers)
#-------------------------------------------
#вывод времени выполнения(1,5 сек для 10^6 и 15 сек для 10^7)
print("--- %s seconds ---" % (time.time() - start_time))
input()