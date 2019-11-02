a, b = [int(i) for i in input().split() ] #ввод нескольких чисел через пробел

#continue #- пропуск хода
#break #- выход из цикла
L =[]  #пустой список 
L.append (128)  #добавление числа в конец списка
L.append (222)

G = [10, 16, 16, 16, 54, 6753, 2452, 235636]
G.extend(L)  # добавление списка L в список G
G.insert(0, 1000) #добавление на 1 место число 1000
G.remove(16) #удаление числа 16 из списка
G.pop(1)  #удаление 2 элемента из списка
G.pop()  #удаление из списка последнего эл-та
print (G.index (235636), "\n") #вывод интекса элемента 
print( G.count(16), "\n") #вывод количества элеиентов с указанным номером
G.sort()    #сортировка списка (по возрастанию)
G.reverse()   #переворот списка
print(G[2])    #вывод 3 го элемента списка


G.clear()  #очистка списка
 
import time
start_time = time.time()
print("--- %s seconds ---" % (time.time() - start_time))

pyinstaller -F 
raise SystemExit

print ('Завершение программы через 3 секунд')
for i in range(3,0,-1):
	time.sleep(1)
	print (i)

import sys
print(sys.platform)

git remote add origin https://github.com/FriLDD/-d.git
git push -u origin master