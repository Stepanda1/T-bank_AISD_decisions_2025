import sys

def last_non_zero_digit(n):
    res = 1
    for i in range(2, n + 1):
        res *= i
        while res % 10 == 0:
            res //= 10
        res %= 100000  # ограничиваем размер числа
    return res % 10

def main():
    n = int(sys.stdin.readline())
    print(last_non_zero_digit(n))

if __name__ == "__main__":
    main()
