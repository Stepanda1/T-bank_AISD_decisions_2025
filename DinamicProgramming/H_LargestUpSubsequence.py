def main():
    n = int(input())
    a = list(map(int, input().split()))
    dp = [1]*n
    prev = [-1]*n
    
    best_len = 1
    best_end = 0
    
    for i in range(n):
        for j in range(i):
            if a[j] < a[i] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                prev[i] = j
        if dp[i] > best_len:
            best_len = dp[i]
            best_end = i
    
    lis = []
    cur = best_end
    while cur != -1:
        lis.append(a[cur])
        cur = prev[cur]
    lis.reverse()
    
    print(best_len)
    print(*lis)
    
if __name__ == "__main__":
    main()