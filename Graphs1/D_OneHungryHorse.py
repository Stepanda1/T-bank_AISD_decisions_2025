from collections import deque

def is_valid(x, y, N):
    return 1 <= x <= N and 1 <= y <= N

def knight_shortest_path(N, x1, y1, x2, y2):
    moves = [
        (2, 1), (1, 2), (-1, 2), (-2, 1),
        (-2, -1), (-1, -2), (1, -2), (2, -1)
    ]
    
    visited = [[False] * (N + 1) for _ in range(N + 1)]
    parent = [[None] * (N + 1) for _ in range(N + 1)]

    queue = deque()
    queue.append((x1, y1))
    visited[x1][y1] = True

    while queue:
        x, y = queue.popleft()
        if (x, y) == (x2, y2):
            break
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny, N) and not visited[nx][ny]:
                visited[nx][ny] = True
                parent[nx][ny] = (x, y)
                queue.append((nx, ny))

    # Восстановление пути
    path = []
    cur = (x2, y2)
    while cur:
        path.append(cur)
        cur = parent[cur[0]][cur[1]]
    path.reverse()

    print(len(path) - 1)
    for px, py in path:
        print(px, py)

# Чтение входных данных
def main():
    N = int(input())
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    knight_shortest_path(N, x1, y1, x2, y2)

if __name__ == "__main__":
    main()
