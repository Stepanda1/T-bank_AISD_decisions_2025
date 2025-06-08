def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    
    class Fenwick:
        def __init__(self,n):
            self.n = n
            self.f = [0]*(n+1)
        def update(self,i,delta):
            while i <= self.n:
                self.f[i] += delta
                i += i & -i
        def query(self,i):
            s = 0
            while i > 0:
                s += self.f[i]
                i -= i & -i
            return s
        def find_kth(self, k):
            idx = 0
            bit_mask = 1 << (self.n.bit_length())
            while bit_mask:
                nxt = idx + bit_mask
                if nxt <= self.n and self.f[nxt] < k:
                    k -= self.f[nxt]
                    idx = nxt
                bit_mask >>= 1
            return idx + 1
        
    fenw = Fenwick(n)
    for i,v in enumerate(a, start=1):
        if v:
            fenw.update(i,1)
            
    out = []
    for _ in range(m):
        parts = input().split()
        typ = parts[0]
        if typ == '1':
            i = int(parts[1])
            if a[i] == 1:
                fenw.update(i+1,-1)
                a[i] = 0
            else:
                fenw.update(i+1,1)
                a[i] = 1
        else:
            k = int(parts[1])
            pos = fenw.find_kth(k+1)
            out.append(str(pos-1))
            
    print('\n'.join(out))
    
if __name__ == "__main__":
    main()