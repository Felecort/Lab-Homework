def determinant(p):
	T = 1
	lst = list(p)
	for i in range(len(lst) // 2):	
		if lst[0] == lst[-1]:
			lst.pop(0)
			lst.pop(-1)
		else:
			T = 0
			break
	if T == 1:
		print(p, "- палиндром")
	else:
		print(p, "- не является палиндромом")
p = input("введите слово/число ")
for j in range(len(list(p))):
	assert list(p)[j] != "/"
	assert list(p)[j] != "*"
	assert list(p)[j] != "-"
	assert list(p)[j] != "+"
determinant(p)



#lol




