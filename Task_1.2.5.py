"""
(1 балл) Вы разработчик игр и работаете над новой фичей (функцией) для игры.
Сейчас надо реализовать логику работы сражений в игре. Во время сражения игрока
с противником каждый наносит удар. У кого сила удара больше, тот и нанес урон.
Противники в игре — боты. За них никто не играет. Поэтому силу удара надо
формировать случайно. Напишите функцию, которая выдает псевдослучайное число
силы удара. Сделайте это с помощью линейного конгруэнтного метода.
"""


def rand_(lcg_):
	a = 1140671485
	c = 128201163
	m = (1 << 32) // 1000000
	return (lcg_ * a + c) % m


if __name__ == "__main__":
	lcg = 88  # Seed
	lcg = rand_(lcg)
	lcg = rand_(lcg)
	...
