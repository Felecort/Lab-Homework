#(6 балла, Yandex) Перепишите функцию из №4.1.1 так, чтобы она проверяла 
#на палиндромом строки. При этом проверяются только буквы и цифры, 
#остальные символы надо пропускать. Напишите тесты.
def palindrom(text):
	txt = text
	i = 0
	lst = list(text)
	lenght = len(lst)
	while lenght > i:
		if lst[i] == " " or lst[i] == "." or lst[i] == "," or lst [i] == "!":
			lst.pop(i)
			lenght -= 1
			i -= 1 
		i += 1
	for j in range(lenght // 2):
		if lst[0] == lst[-1]:
			lst.pop(0)
			lst.pop(-1)
		else:
			T = 0
			return txt + "- не палиндром"
	return txt + "- палиндром"
print(palindrom("колесо.,!, жалко поклаж. оселок."))




