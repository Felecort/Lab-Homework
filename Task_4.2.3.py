class AB:
    ab = {}
    def __init__(self, key, value):
        self.key = key
        self.value = value
        AB.ab[key] = value
 
    @staticmethod
    def add():
        name = input('Введите имя: ')
        address = input('Введите адрес: ')
        obj = AB(name,address)
        print("Элемент добавлен")
 
    @staticmethod
    def delete():
        name = input('Введите имя: ')
        del AB.ab[name]
 
    @staticmethod
    def printOut():
        for i in AB.ab.items():
            print(i)
 
    @staticmethod
    def change():
       name = input('Введите имя: ')
       AB.ab[name] = input("Новое значение :")
 
    @staticmethod
    def view(name):
        print(AB.ab[name])
 
 
 
 
    @staticmethod
    def menu():
        x = -1
        while x != '6':
            print('''1. Вывод - 1\n2. Добавить - 2 \n3. Удалить - 3 \n4. Задать ключ - 4 \n5. Посотреть по ключу - 5 \n6. Выход - 6 ''')
            x = input('Введите значение : ')
            if x == '1':
                AB.printOut()
            elif x =='2':
                AB.add()
            elif x == '3':
                AB.delete()
            elif x == '4':
                AB.change()
            elif x == '5':
                a.key=input()
                AB.view(a.key)
            elif x == '6':
                break
 
a = AB('Alex','street1')
b = AB('Nadezhda','street2')
AB.menu()