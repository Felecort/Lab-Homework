#(6 балла, Yandex) Перепишите функцию из №4.1.1 так, чтобы она проверяла 
#на палиндромом строки. При этом проверяются только буквы и цифры, 
#остальные символы надо пропускать. Напишите тесты.isalnum


def palindrom(text):
	length = len(text)
	for i in range(0, length):
		if not text[i].isalnum():
			length -= 1 
	if length != 0:
		i = 0
		j = -1
		while  i < len(text) // 2:
			while text[i].isalnum() == False:
				i += 1
			while text[j].isalnum() == False:
				j -= 1
			if text[i] == text[j]:
				i += 1
				j -= 1
			else: return False
#Символы, крому букв и цифр в данной задаче приравниваются к "",
#следовательно "" - палиндром, "*?" - палиндром
	return True
print(palindrom("***")) 				#true
print(palindrom("aa&*aa$(aa"))				#true
print(palindrom(" )u + j*/-"))						#false

if __name__ == "__main__":
    import doctest
    doctest.testmod()
