"""
(1 балл) Вы разработчик игр и разбираетесь с жалобами игроков.
Многие ругаются, что герои часто застревают в текстурах. Оказалось, что функция,
которая проверяет пересечение фигуры героя со стенами написана с ошибкой.
Надо переписать. Напишите функцию, которая проверяет пересекаются ли два
прямоугольника. Они заданы двумя точками диагонали, стороны параллельны осям
декартовой системы координат. Можно ли переписать программу так, чтобы она
выдавала координаты пересечения?
"""


def is_rectangles_intersection(coord1: list, coord2: list) -> bool:
    ax1, ay1 = coord1[0]
    ax2, ay2 = coord1[1]
    bx1, by1 = coord2[0]
    bx2, by2 = coord2[1]
    s1 = (ax1 >= bx1 and ax1 <= bx2) or (ax2 >= bx1 and ax2 <= bx2)
    s2 = (ay1 >= by1 and ay1 <= by2) or (ay2 >= by1 and ay2 <= by2)
    s3 = (bx1 >= ax1 and bx1 <= ax2) or (bx2 >= ax1 and bx2 <= ax2)
    s4 = (by1 >= ay1 and by1 <= ay2) or (by2 >= ay1 and by2 <= ay2)

    return True if ((s1 and s2) or (s3 and s4)) or ((s1 and s4) or (s3 and s2)) else False


if __name__ == "__main__":
    f1 = [[1, 1], [5, 5]]
    f2 = [[3, 3], [7, 75]]
    print(is_rectangles_intersection(f1, f2))
