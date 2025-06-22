import math

def factorize(n):
    result = []
    for i in range(2, int(math.isqrt(n)) + 1):
        count = 0
        while n % i == 0:
            n //= i
            count += 1
        if count > 0:
            result.append((i,count))
    if n > 1:
        result.append((n,1))
    return result

def format_factors(factors):
    parts = []
    for base, power in factors:
        if power == 1:
            parts.append(str(base))
        else:
            parts.append(f"{base}^{power}")
    return '*'.join(parts)

def main():
    n = int(input())
    factors = factorize(n)
    print(format_factors(factors))
    
if __name__ == "__main__":
    main()