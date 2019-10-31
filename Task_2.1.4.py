#2 балла) В репозитории курса есть пакет с некоторыми примерами 
#алгоритмов поиска. С помощью функции time из одноименного пакета 
#замерьте время поиска на списках разной длины. Какой алгоритм самый 
#быстрый? Будет ли работать быстрее бинарный поиск, если предварительно 
#числять верхнюю границу списка (см. экспоненциальный поиск)?

import time
array = []
start_time = time.time()
for data in range(5000001):
    array.append(data) 
print("время заполнения массива %s seconds " % (time.time() - start_time))

start_time = time.time()
from algorithms import linear
print(linear(5000000, array))
print("линейный поиск 			 %s seconds " % (time.time() - start_time))



start_time = time.time()
from algorithms import binary
print(binary(5000000, array))
print("бинарный поиск 			 %s seconds " % (time.time() - start_time))


start_time = time.time()
from algorithms import interpolation
print(interpolation(5000000, array))
print("интерполяционный поиск   %s seconds" % (time.time() - start_time))