#(6 балла, Yandex) Перепишите функцию из №4.1.1 так, чтобы она проверяла 
#на палиндромом строки. При этом проверяются только буквы и цифры, 
#остальные символы надо пропускать. Напишите тесты.isalnum
def palindrom(text):
	assert text != ""
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
	return True
print(palindrom("!@# $%^&*  lol&^l ol*")) 	#true
print(palindrom("aa&*aa$(aa"))				#true
print(palindrom("klll&*"))					#false
print(palindrom("a1001a"))					#true
print(palindrom("1212"))					#false	