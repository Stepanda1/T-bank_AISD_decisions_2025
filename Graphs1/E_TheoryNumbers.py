import heapq

def min_digit_sum_divisible_by_k(K):
    dist = [float('inf')] * K
    heap = []

    for d in range(1, 10):
        r = d % K
        if dist[r] > d:
            dist[r] = d
            heapq.heappush(heap, (d, r))

    while heap:
        digit_sum, rem = heapq.heappop(heap)

        if rem == 0:
            return digit_sum

        for d in range(10):
            new_rem = (rem * 10 + d) % K
            new_sum = digit_sum + d
            if dist[new_rem] > new_sum:
                dist[new_rem] = new_sum
                heapq.heappush(heap, (new_sum, new_rem))

# Основной ввод
def main():
    K = int(input())
    print(min_digit_sum_divisible_by_k(K))

if __name__ == "__main__":
    main()
