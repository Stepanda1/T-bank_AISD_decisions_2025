def can_split(arr, n, k, max_sum):
    # Проверка, можно ли разделить массив на k отрезков, 
    # так чтобы максимальная сумма в каждом отрезке не превышала max_sum
    current_sum = 0
    segments = 1  # начинаем с первого сегмента
    
    for num in arr:
        if current_sum + num > max_sum:
            segments += 1
            current_sum = num  # начинаем новый сегмент
            if segments > k:  # если сегментов больше, чем k, возвращаем False
                return False
        else:
            current_sum += num
    
    return True

def solve():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    
    # Инициализация диапазона для бинарного поиска
    left, right = max(arr), sum(arr)
    
    # Бинарный поиск по максимальной сумме на отрезке
    while left < right:
        mid = (left + right) // 2
        if can_split(arr, n, k, mid):
            right = mid  # если можно разбить, пробуем уменьшить максимальную сумму
        else:
            left = mid + 1  # если нельзя разбить, увеличиваем минимальную сумму
    
    print(left)

if __name__ == "__main__":
    solve()
