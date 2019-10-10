def determinant(p):
	o = p[::-1]
	if o == p:
		print(p, "- палиндром")
	else:
		print(p, "- не является палиндромом")
p = input("введите слово/число ")
determinant(p)