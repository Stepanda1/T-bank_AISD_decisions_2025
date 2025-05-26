def main():
    n, m = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(m)]
    permutation = list(map(int, input().split()))

    position = [0] * (n + 1)
    for i, node in enumerate(permutation):
        position[node] = i

    for u, v in edges:
        if position[u] >= position[v]:
            print("NO")
            return

    print("YES")

if __name__ == "__main__":
    main()
