from collections import deque, defaultdict

def main():
    m = int(input())
    graph = defaultdict(list)

    for _ in range(m):
        line = input().strip()
        if '->' in line:
            a, b = map(str.strip, line.split('->'))
            graph[a].append(b)

    start = input().strip()
    goal = input().strip()

    if start == goal:
        print(0)
        return

    # BFS
    visited = set()
    queue = deque([(start, 0)])

    while queue:
        current, dist = queue.popleft()
        if current == goal:
            print(dist)
            return
        visited.add(current)
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, dist + 1))

    print(-1)

if __name__ == "__main__":
    main()
