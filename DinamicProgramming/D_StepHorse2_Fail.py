import sys

def count_paths(n, m):
    # dp[i][j] = число способов добраться до клетки (i,j), 1-based
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    dp[1][1] = 1
    moves = [(2,1), (1,2), (-1,2), (2,-1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == 1 and j == 1:
                continue
            total = 0
            for di, dj in moves:
                pi, pj = i - di, j - dj
                if 1 <= pi <= n and 1 <= pj <= m:
                    total += dp[pi][pj]
            dp[i][j] = total
    return dp[n][m]

def main():
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        parts = line.split()
        # Ожидаем либо 2 числа: n m
        if len(parts) != 2:
            continue
        n, m = map(int, parts)
        print(count_paths(n, m))

if __name__ == "__main__":
    main()