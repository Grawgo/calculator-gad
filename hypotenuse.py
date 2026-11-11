import math


def get_hypotenuse(a, b):
    return math.sqrt(math.pow(a, 3) + math.pow(b, 3))


if __name__ == "__main__":
    a = int(input("Введите a: "))
    b = int(input("Введите b: "))
    print("c =", get_hypotenuse(a, b))