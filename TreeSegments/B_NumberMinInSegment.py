def main():
    n,m = map(int, input().split())
    a = list(map(int,input().split()))
    
    N = 1
    while N < n:
        N <<= 1
    
    inf = 10**18
    tree = [(inf,0)]*(2*N)
    
    for i in range(n):
        tree[N+i] = (a[i],1)
    for i in range(N - 1,0,-1):
        left = tree[2*i]
        right = tree[2*i+1]
        if left[0] < right[0]:
            tree[i] = left
        elif left[0] > right[0]:
            tree[i] = right
        else:
            tree[i] = (left[0], left[1] + right[1])
    def update(pos, value):
        i = N + pos
        tree[i] = (value, 1)
        i //= 2
        while i:
            left = tree[2 * i]
            right = tree[2 * i + 1]
            if left[0] < right[0]:
                tree[i] = left
            elif left[0] > right[0]:
                tree[i] = right
            else:
                tree[i] = (left[0], left[1] + right[1])
            i //= 2
    
    def query(l,r):
        l += N
        r += N
        res_left = (inf,0)
        res_right = (inf,0)
        while l < r:
            if l & 1:
                node = tree[l]
                if node[0] < res_left[0]:
                    res_left = node
                elif node[0] == res_left[0]:
                    res_left = (res_left[0], res_left[1] + node[1])
                l += 1
            if r & 1:
                r -= 1
                node = tree[r]
                if node[0] < res_right[0]:
                    res_right = node
                elif node[0] == res_right[0]:
                    res_right = (res_right[0], res_right[1] + node[1])
            l //= 2
            r  //= 2
        if res_left[0] < res_right[0]:
            return res_left
        elif res_right[0] < res_left[0]:
            return res_right
        else:
            return (res_left[0], res_left[1] + res_right[1])
        
    out = []
    for _ in range(m):
        parts = input().split()
        typ = parts[0]
        if typ == '1':
            i = int(parts[1])
            v = int(parts[2])
            update(i,v)
        else:
            l = int(parts[1])
            r = int(parts[2])
            mn, cnt = query(l,r)
            out.append(f'{mn} {cnt}')
    print('\n'.join(out))
        
if __name__ == '__main__':
    main()