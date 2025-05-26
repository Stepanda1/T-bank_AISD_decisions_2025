def solve():
    # Чтение входных данных
    N, M, K = map(int, input().split())
    
    # Матрица данных
    matrix = [list(map(int, input().split())) for _ in range(N)]
    
    # Префиксные суммы
    prefix = [[0] * (M + 1) for _ in range(N + 1)]
    
    # Строим префиксные суммы
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            prefix[i][j] = (matrix[i - 1][j - 1] 
                            + prefix[i - 1][j] 
                            + prefix[i][j - 1] 
                            - prefix[i - 1][j - 1])
    
    # Обработка запросов
    for _ in range(K):
        y1, x1, y2, x2 = map(int, input().split())
        
        # Рассчитываем сумму на прямоугольном участке с помощью префиксных сумм
        result = (prefix[y2][x2]
                 - prefix[y1 - 1][x2]
                 - prefix[y2][x1 - 1]
                 + prefix[y1 - 1][x1 - 1])
        
        print(result)

if __name__ == "__main__":
    solve()
