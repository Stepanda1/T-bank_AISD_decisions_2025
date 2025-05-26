import sys

def max_good_days():
    # Читаем входные данные
    n = int(sys.stdin.readline().strip())
    arr = list(map(int, sys.stdin.readline().split()))
    
    # Префиксные суммы для быстрого вычисления суммы подотрезка
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + arr[i]

    # Стек для нахождения ближайшего меньшего элемента слева
    left = [-1] * n
    stack = []
    for i in range(n):
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()
        left[i] = stack[-1] if stack else -1
        stack.append(i)

    # Стек для нахождения ближайшего меньшего элемента справа
    right = [n] * n
    stack = []
    for i in range(n - 1, -1, -1):
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()
        right[i] = stack[-1] if stack else n
        stack.append(i)

    # Поиск максимального значения выражения
    max_value = 0
    for i in range(n):
        l, r = left[i], right[i]  # Границы отрезка, где arr[i] — минимум
        subarray_sum = prefix_sum[r] - prefix_sum[l + 1]  # Быстро считаем сумму через префикс
        max_value = max(max_value, subarray_sum * arr[i])

    print(max_value)

max_good_days()
