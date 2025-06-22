def mod_pow(a,b,mod):
    result = 1
    a %= mod
    while b > 0:
        if b % 2:
            result = result * a % mod
        a = a * a % mod
        b //= 2
    return result

def mod_inverse(k, mod):
    return mod_pow(k, mod-2, mod)

N,M,K,MOD = map(int, input().split())

power = mod_pow(M,N,MOD)

inverse_k = mod_inverse(K,MOD)

result = power * inverse_k % MOD
print(result)