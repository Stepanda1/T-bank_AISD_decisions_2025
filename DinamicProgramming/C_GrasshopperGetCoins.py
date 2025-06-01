from collections import deque

def main():
    # 1) Читаем n и k одной строкой
    n, k = map(int, input().split())

    # 2) Читаем второй строкой n−2 целых чисел (монеты на столбиках 2..n−1)
    vals = list(map(int, input().split()))
    # Заводим массив val длины (n+1), чтобы индексировать с 1 до n
    val = [0] * (n + 1)
    for i in range(2, n):
        val[i] = vals[i - 2]
    # val[1] и val[n] остаются равными 0

    # 3) Создаём dp и prev
    # dp[i] = максимальное число монет, добираясь до столбика i
    INF = 10**18
    dp = [-INF] * (n + 1)
    dp[1] = 0
    # prev[i] = предыдущий столбик на оптимальном пути к i
    prev = [0] * (n + 1)

    # 4) Дек для «скользящего максимума» на отрезке [i-k .. i-1]
    deq = deque([1])  # сначала доступен только столбик 1

    for i in range(2, n + 1):
        # 4.1) Убираем из головы все индексы < i − k
        while deq and deq[0] < i - k:
            deq.popleft()

        # 4.2) Берём j = deq[0] — индекс с максимальным dp[j] в «окне»
        j = deq[0]
        dp[i] = dp[j] + val[i]
        prev[i] = j

        # 4.3) Вставляем i в хвост, удаляя из хвоста все t с dp[t] ≤ dp[i]
        while deq and dp[deq[-1]] <= dp[i]:
            deq.pop()
        deq.append(i)

    # 5) Восстанавливаем путь от n до 1 по prev[]
    path = []
    cur = n
    while cur != 0:
        path.append(cur)
        cur = prev[cur]
    path.reverse()

    total_coins = dp[n]
    jumps = len(path) - 1

    # 6) Выводим результат
    print(total_coins)
    print(jumps)
    print(" ".join(map(str, path)))


if __name__ == "__main__":
    main()
