def count_less_equal(x, n):
    count = 0
    for i in range(1, n + 1):
        count += min(x // i, n)
    return count

def solve():
    n, k = map(int, input().split())

    left, right = 1, n * n
    answer = 0

    while left <= right:
        mid = (left + right) // 2
        if count_less_equal(mid, n) >= k:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    print(answer)

if __name__ == "__main__":
    solve()
