"""
(1 балл) На чемпионате The Internetional в следующем году
будет участвовать много команд. Сколько существует вариантов
распределить первые три места? А все места? Напишите функцию,
которая вычисляет эти значения.
"""


def fact(n):
    factorial = 1
    for i in range(2, n + 1):
        factorial *= i
    return factorial

if __name__ == "__main__":
    count_comands = 12
    fact2 = count_comands - 3

    print("Варианты распределения всем местам:", fact(count_comands))
    print("Варианты распределения первым 3м местам:", (fact(count_comands) // fact(fact2)))