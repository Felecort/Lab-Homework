factorial = int( input("Введите количество команд ") )
fact2 = factorial - 3
def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)
print("количесвто вариантов распределения всем местам = ", str(fact(factorial)) )
print("количесвто вариантов распределения первым 3м местам= ", (fact(factorial)/fact(fact2)))