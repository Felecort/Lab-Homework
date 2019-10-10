def count(m, k, l):

	#Алгоритм Евклида
	def Euclidean_Algorithm(a, b):
		while a != b:
			if a > b:
				a = a - b
			else:
				b = b - a
		return b
	print((((m * k) / Euclidean_Algorithm(m, k) * l) / Euclidean_Algorithm(k, l)))
	
	# более читабельный для человека вариант:
	#q = (m * k) / Euclidean_Algorithm(m, k)
	#w = Euclidean_Algorithm(k, l)
	#print( q * l / w)

count(12, 12, 24)