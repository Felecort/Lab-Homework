#(2 балла) В системе регистрации сайта был сбой и в списке 
#идентификаторов пользователей есть повторяющиеся идентификаторы. 
#Напишите функцию, которая проверяет есть ли повторы в списке. 
#Попробуйте найти решение за квазилинейное время.
#ℹ️ Подсказка
#Что будет, если сначала отсортировать?

def iteration(list_of_identifiers):
	duplicate_identifiers = []
	for i in range(len(list_of_identifiers)-1):
		if list_of_identifiers[i] == list_of_identifiers[i+1]:
			duplicate_identifiers.append(list_of_identifiers[i])
	return duplicate_identifiers
list_of_identifiers = [475,45,95,7,46,43,1,978,897,24,4987,98,75,15,36,85,132,94,25,74,22,565]
list_of_identifiers.sort()
print("Дубликаты идентификаторов: ", iteration(list_of_identifiers))
   