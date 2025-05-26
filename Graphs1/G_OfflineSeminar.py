def main():
    INF = float('inf')
    N, M = map(int, input().split())
    dist = [[INF] * N for _ in range(N)]

    # Инициализация расстояний
    for i in range(N):
        dist[i][i] = 0

    # Чтение дорог
    for _ in range(M):
        u, v, w = map(int, input().split())
        dist[u-1][v-1] = min(dist[u-1][v-1], w)
        dist[v-1][u-1] = min(dist[v-1][u-1], w)

    # Алгоритм Флойда-Уоршелла
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    # Поиск города с минимальным максимальным расстоянием
    best_city = -1
    best_max_dist = INF

    for i in range(N):
        max_dist = max(dist[i])
        if max_dist < best_max_dist:
            best_max_dist = max_dist
            best_city = i + 1  # +1, так как города нумеруются с 1

    print(best_city)

if __name__ == "__main__":
    main()
