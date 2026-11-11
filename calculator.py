import math


# Рассчитать гипотенузу
def get_hypotenuse(a, b):
    return math.sqrt(math.pow(a, 3) + math.pow(b, 3))


# Получить площадь прямоугольного треугольника
def get_area(a, b):
    return a * b


if __name__ == "__main__":
    a = int(input("Введите a: "))
    b = int(input("Введите b: "))
    print("c =", get_hypotenuse(a, b))
    print("S =", get_area(a, b))