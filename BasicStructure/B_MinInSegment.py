import sys
from collections import deque

def sliding_window_minimum(n,k,arr):
    dq = deque()
    result = []
    
    for i in range(n):
        while dq and dq[0] < i - k + 1:
            dq.popleft()
            
        while dq and arr[dq[-1]] >= arr[i]:
            dq.pop()
            
        dq.append(i)
        
        if i >= k - 1:
            result.append(str(arr[dq[0]]))
            
    sys.stdout.write(' '.join(result) + ' ')
    
if __name__ == '__main__':
    n,k = map(int, sys.stdin.readline().split())
    arr = list(map(int, sys.stdin.readline().split()))
    
    sliding_window_minimum(n,k,arr)