import sys
sys.setrecursionlimit(10**7)

def dfs(v, visited, component, graph):
    visited[v] = True
    component.append(v)
    for neighbor in graph[v]:
        if not visited[neighbor]:
            dfs(neighbor, visited, component, graph)

def main():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    visited = [False] * (n + 1)
    components = []

    for i in range(1, n + 1):
        if not visited[i]:
            component = []
            dfs(i, visited, component, graph)
            components.append(sorted(component))

    print(len(components))
    for comp in components:
        print(len(comp))
        print(" ".join(map(str, comp)))

if __name__ == "__main__":
    main()
