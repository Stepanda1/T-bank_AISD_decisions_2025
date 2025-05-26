def can_place_cows(stalls, K, min_dist):
    # Проверка, можем ли разместить K коров с минимальным расстоянием min_dist
    count = 1  # Размещаем первую корову в первом стойле
    last_position = stalls[0]

    for i in range(1, len(stalls)):
        if stalls[i] - last_position >= min_dist:
            count += 1
            last_position = stalls[i]
            if count == K:  # Если мы разместили все коров
                return True
    return False

def solve():
    # Чтение входных данных
    N, K = map(int, input().split())
    stalls = list(map(int, input().split()))

    # Бинарный поиск по минимальному расстоянию
    left = 1  # Минимальное возможное расстояние
    right = stalls[-1] - stalls[0]  # Максимальное возможное расстояние

    best_dist = 0

    while left <= right:
        mid = (left + right) // 2
        if can_place_cows(stalls, K, mid):
            best_dist = mid  # Если можно разместить коров с таким расстоянием, пробуем больше
            left = mid + 1
        else:
            right = mid - 1

    print(best_dist)

if __name__ == "__main__":
    solve()
