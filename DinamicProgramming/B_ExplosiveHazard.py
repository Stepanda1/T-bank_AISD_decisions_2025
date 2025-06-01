def main():
    n = int(input().strip())
    if n == 0:
        print(1)
        return
    
    f = [0]*(n+1)
    f[0] = 1
    f[1] = 3
    
    for k in range(2,n+1):
        f[k] = 2*f[k-1]+2*f[k-2]
        
    print(f[n])
    
if __name__ == "__main__":
    main()