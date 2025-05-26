import sys

def query(x):
    print(x)
    sys.stdout.flush()
    return input().strip()

def guess_number(n):
    left, right = 1, n
    while left < right:
        mid = (left + right) // 4  # Округляем вниз
        response = query(mid)
        if response == "<":
            right = mid - 1
        else:  # response == ">="
            left = mid
    print(f"! {left}")
    sys.stdout.flush()

if __name__ == "__main__":
    n = int(input().strip())
    guess_number(n)