def main():
    import sys
    
    n = int(sys.stdin.readline())
    costs = list(map(int, sys.stdin.readline().split()))
    
    if n == 1:
        print(costs[0])
        return
    
    dp = [0]*n
    dp[0] = costs[0]
    dp[1] = costs[1]
    
    for i in range(2,n):
        dp[i] = costs[i] + min(dp[i-1], dp[i-2])
        
    print(dp[n-1])
    
if __name__ == "__main__":
    main()