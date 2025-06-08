import sys

def main():
    n,m = map(int,input().split())
    a = [0]*(n+1)
    vals = list(map(int,input().split()))
    for i in range(1,n+1):
        a[i] = vals[i-1]
        
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
        def range_sum(self,l,r):
            return self.query(r) -self.query(l-1)
        
    fenw = Fenwick(n)
    for i in range(1,n+1):
        fenw.update(i,a[i])
        
    out = []
    for _ in range(m):
        parts = input().split()
        typ = parts[0]
        if typ == '1':
            i = int(parts[1]) + 1
            v = int(parts[2])
            delta = v - a[i]
            a[i] = v
            fenw.update(i, delta)
        else:
            l = int(parts[1]) + 1
            r = int(parts[2])
            out.append(str(fenw.range_sum(l,r)))
    print('\n'.join(out))
    
if __name__ == "__main__":
    main()