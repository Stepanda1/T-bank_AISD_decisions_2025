import sys
sys.setrecursionlimit(10**7)

def dfs(v, graph, visited):
    visited[v] = 1  # серый
    for neighbor in graph[v]:
        if visited[neighbor] == 0:  # белый
            if dfs(neighbor, graph, visited):
                return True
        elif visited[neighbor] == 1:  # серый => цикл
            return True
    visited[v] = 2  # чёрный
    return False

def main():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)

    visited = [0] * (n + 1)  # 0: белый, 1: серый, 2: чёрный

    for i in range(1, n + 1):
        if visited[i] == 0:
            if dfs(i, graph, visited):
                print(1)
                return
    print(0)

if __name__ == "__main__":
    main()
