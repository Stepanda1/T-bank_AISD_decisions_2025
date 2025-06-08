import sys

def main():
    input = sys.stdin.readline
    MOD = 10**9 + 7

    n = int(input())
    a = list(map(int, input().split()))

    # Coordinate compression
    coords = sorted(set(a))
    comp = {v: i for i, v in enumerate(coords, start=1)}
    m = len(coords)

    # BIT arrays for (length, count)
    size = m + 1
    bit_len = [0] * (size + 1)
    bit_cnt = [0] * (size + 1)

    def bit_query(idx):
        best_len = 0
        total_cnt = 0
        while idx > 0:
            l = bit_len[idx]
            c = bit_cnt[idx]
            if l > best_len:
                best_len, total_cnt = l, c
            elif l == best_len:
                total_cnt = (total_cnt + c) % MOD
            idx -= idx & -idx
        return best_len, total_cnt

    def bit_update(idx, length, count):
        while idx <= size:
            l = bit_len[idx]
            c = bit_cnt[idx]
            if length > l:
                bit_len[idx], bit_cnt[idx] = length, count
            elif length == l:
                bit_cnt[idx] = (c + count) % MOD
            idx += idx & -idx

    # Process sequence
    for v in a:
        i = comp[v]
        prev_len, prev_cnt = bit_query(i - 1)
        if prev_len == 0:
            curr_len, curr_cnt = 1, 1
        else:
            curr_len, curr_cnt = prev_len + 1, prev_cnt
        bit_update(i, curr_len, curr_cnt)

    # Answer is total count of max-length subsequences
    _, result = bit_query(size)
    print(result)

if __name__ == "__main__":
    main()
