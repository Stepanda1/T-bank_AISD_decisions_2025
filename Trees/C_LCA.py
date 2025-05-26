import sys
import math

sys.setrecursionlimit(200000)

# Чтение входных данных
def solve():
    n = int(input())  # Количество вершин
    parent = list(map(int, input().split()))  # Родители для каждой вершины
    m = int(input())  # Количество запросов
    queries = [tuple(map(int, input().split())) for _ in range(m)]  # Запросы
    
    LOG = int(math.log2(n)) + 1  # Максимальное количество уровней для бинарного подъема
    up = [[-1] * LOG for _ in range(n)]  # Таблица для хранения родителей на разных уровнях
    depth = [0] * n  # Глубина каждой вершины
    
    # Строим дерево
    for i in range(1, n):
        up[i][0] = parent[i-1]  # Родитель для вершины i
        depth[i] = depth[parent[i-1]] + 1  # Глубина вершины i
    
    # Заполняем таблицу up
    for j in range(1, LOG):
        for i in range(n):
            if up[i][j-1] != -1:
                up[i][j] = up[up[i][j-1]][j-1]
    
    # Функция для нахождения LCA двух вершин u и v
    def lca(u, v):
        if depth[u] < depth[v]:
            u, v = v, u
        
        # Поднимаем u на уровень v
        for i in range(LOG-1, -1, -1):
            if depth[u] - (1 << i) >= depth[v]:
                u = up[u][i]
        
        if u == v:
            return u
        
        # Поднимаем оба узла до тех пор, пока они не станут одинаковыми
        for i in range(LOG-1, -1, -1):
            if up[u][i] != up[v][i]:
                u = up[u][i]
                v = up[v][i]
        
        # Возвращаем родителя
        return up[u][0]
    
    # Обрабатываем запросы
    for u, v in queries:
        print(lca(u, v))

if __name__ == "__main__":
    solve()
