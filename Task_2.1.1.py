import random
import time
idd = []
dub = []
c = 10000

#функция поиска повторяющихся элементов
def iteration(idd):
	for j in range(c-1):
		if idd[j] == idd[j+1]:
			dub.append(idd[j])
		else: pass


#Заполнение массива данными
for i in range(c):
	a = random.randint(3000, 7000)
	idd.append(a)
idd.sort()


start_time = time.time ()
iteration(idd)
print("время поиска повторяющихся элементов = %s секунд" % (time.time() - start_time))


dub.insert(0, "Имеются дубликаты идентификаторов:")
print(dub)

