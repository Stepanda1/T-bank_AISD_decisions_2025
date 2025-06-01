def main():
    import sys
    sys.setrecursionlimit(10000)
    s = input()
    n = len(s)
    dp = [[0] * n for _ in range(n)]
    choice = [[None] * n for _ in range(n)]
    
    def matches(a,b):
        return (a == '(' and b == ')') or (a == '[' and b == ']') or (a == '{' and b == '}')
    
    for length in range(1, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            best = 0
            choice[i][j] = -1
            if i + 1 <= j:
                best = dp[i + 1][j]
            else:
                best = 0
                
            for k in range(i + 1, j + 1):
                if matches(s[i], s[k]):
                    mid = 0 if i + 1 > k - 1 else dp[i+1][k-1]
                    right = 0 if k + 1 > j else dp[k+1][j]
                    cur = 2 + mid + right
                    if cur > best:
                        best = cur
                        choice[i][j] = k
            dp[i][j] = best
    
    def build(i,j):
        if i > j:
            return ''
        if choice[i][j] == -1:
            return build(i + 1, j)
        k = choice[i][j]
        if k is None:
            return ''
        inside = build(i + 1, k - 1)
        after = build(k + 1, j)
        return s[i] + inside + s[k] + after

    result = build(0, n - 1)
    print(result)

if __name__ == "__main__":
    main()