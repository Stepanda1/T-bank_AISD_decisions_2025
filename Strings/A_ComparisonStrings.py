def main():
    import sys
    input = sys.stdin.readline

    s = input().strip()  # Строка
    m = int(input())  # Количество запросов
    n = len(s)

    # Параметры для хеширования
    mod1 = 10**9 + 7
    mod2 = 10**9 + 9
    base1 = 911
    base2 = 3571

    # Предподсчёт степеней оснований
    pow1 = [1] * (n + 1)
    pow2 = [1] * (n + 1)
    for i in range(1, n + 1):
        pow1[i] = (pow1[i-1] * base1) % mod1
        pow2[i] = (pow2[i-1] * base2) % mod2

    # Предподсчёт префиксных хешей
    h1 = [0] * (n + 1)
    h2 = [0] * (n + 1)
    for i in range(n):
        h1[i+1] = (h1[i] * base1 + ord(s[i])) % mod1
        h2[i+1] = (h2[i] * base2 + ord(s[i])) % mod2

    def get_hash(l, r):
        """Получить хеш подстроки s[l..r] (l и r — 0-индексация)"""
        x1 = (h1[r+1] - h1[l] * pow1[r - l + 1]) % mod1
        x2 = (h2[r+1] - h2[l] * pow2[r - l + 1]) % mod2
        return (x1, x2)

    output = []
    for _ in range(m):
        a, b, c, d = map(int, input().split())
        a -= 1  # Переводим индексы в 0-индексацию
        b -= 1
        c -= 1
        d -= 1
        if b - a != d - c:
            output.append("No")
        else:
            if get_hash(a, b) == get_hash(c, d):
                output.append("Yes")
            else:
                output.append("No")
    
    print('\n'.join(output))

if __name__ == "__main__":
    main()
