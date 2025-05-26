def solve():
    n = int(input())  # количество отрезков
    segments = []
    
    # Чтение всех отрезков
    for _ in range(n):
        li, ri = map(int, input().split())
        segments.append((li, ri))
    
    # Сортируем отрезки по начальной точке (если они равны, то по правой точке)
    segments.sort()
    
    total_length = 0
    current_left, current_right = segments[0]  # Начинаем с первого отрезка
    
    for i in range(1, n):
        left, right = segments[i]
        
        # Если текущий отрезок пересекается или касается предыдущего
        if left <= current_right:
            # Сливаем отрезки, расширяя правую границу
            current_right = max(current_right, right)
        else:
            # Если не пересекаются, то добавляем длину предыдущего отрезка
            total_length += current_right - current_left
            current_left, current_right = left, right
    
    # Добавляем последний отрезок
    total_length += current_right - current_left
    
    print(total_length)

if __name__ == "__main__":
    solve()
