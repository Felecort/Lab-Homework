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
list_of_identifiers = [100, 123, 545, 456, 452, 400, 100, 754, 400, 248]
list_of_identifiers.sort()
print("Дубликаты идентификаторов: ", iteration(list_of_identifiers))
