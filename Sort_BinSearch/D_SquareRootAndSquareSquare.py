import math

def f(x, C):
    return x**2 + math.sqrt(x+1) - C

def find_x(C):
    left, right = 0, C
    precision = 1e-7  # Задаем точность
    while right - left > precision:
        mid = (left + right) / 2
        if f(mid, C) < 0:
            left = mid  # Ищем в правой части
        else:
            right = mid  # Ищем в левой части
    return left  # Возвращаем левую границу, где f(x) примерно равно 0

if __name__ == "__main__":
    C = float(input().strip())
    result = find_x(C)
    print(f"{result:.20f}")  # Форматируем вывод с 10 знаками после запятой