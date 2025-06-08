def main():
    n = int(input())
    a = list(map(int, input().split()))
    
    vals = sorted(set(a))
    comp = {v: i+1 for i,v in enumerate(vals)}
    
    m = len(vals)
    bit = [0]*(m+1)
    def bit_update(i,delta):
        while i <= m:
            bit[i] += delta
            i += i & -i
    def bit_query(i):
        s = 0
        while i > 0:
            s += bit[i]
            i -= i & -i
        return s
    
    left_greater = [0]*n
    seen = 0
    for j in range(n):
        cj = comp[a[j]]
        leq = bit_query(cj)
        left_greater[j] = seen - leq
        bit_update(cj,1)
        seen += 1
        
    bit = [0]*(m+1)
    right_less = [0]*n
    for idx in range(n-1,-1,-1):
        cj = comp[a[idx]]
        right_less[idx] = bit_query(cj-1)
        bit_update(cj,1)
        
    total = 0
    for j in range(n):
        total += left_greater[j] * right_less[j]
    
    print(total)
    
if __name__ == '__main__':
    main()