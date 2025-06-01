def main():
    n,m = map(int, input().split())
    mat = [list(map(int, input().split())) for _ in range(n)]
    
    dp = [[0] * m for _ in range(n)]
    
    best_size = 0
    best_i = 0
    best_j = 0
    
    for i in range(n):
        for j in range(m):
            if mat[i][j] == 1:
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = 1 + min(
                            dp[i-1][j],
                            dp[i][j-1],
                            dp[i-1][j-1]
                        )
                if dp[i][j] > best_size:
                    best_size = dp[i][j]
                    best_i = i
                    best_j = j
                    
    top_i = best_i - best_size + 1
    top_j = best_j - best_size + 1
    
    print(best_size)
    print(top_i + 1, top_j + 1)
    
if __name__ == "__main__":
    main()