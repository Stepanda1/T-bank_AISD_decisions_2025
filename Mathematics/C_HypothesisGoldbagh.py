def sieve(limit):
    is_prime = [True]*(limit + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(limit ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False
    return is_prime
    
def main():
    n = int(input())
    is_prime = sieve(n)
    
    for p in range(2, n // 2 + 1):
        q = n - p
        if is_prime[p] and is_prime[q]:
            print(p, q)
            return
if __name__ == "__main__":
    main()