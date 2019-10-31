					
lcg = int(input("введите сид "))
a = 1140671485				#переменные а, с, м взяты из википедии из соотвествующей статьи
c = 128201163
m = (2**32) // 1000000
def rand(lcg):
	lcg = ((lcg * a + c) % m)
	print ("Нанесённый урон =", lcg)
	return(lcg)
for i in range(2):
	rand(lcg) 