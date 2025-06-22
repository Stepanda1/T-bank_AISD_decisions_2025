#include <iostream>
#include <vector>
using namespace std;

const int MOD = 1e9 + 7;
const int MAXN = 1e6 + 1;

vector<long long> fact(MAXN);
vector<long long> inv_fact(MAXN);

// Быстрое возведение в степень по модулю
long long mod_pow(long long a, long long b, long long mod) {
    long long result = 1;
    a %= mod;
    while (b > 0) {
        if (b % 2 == 1)
            result = result * a % mod;
        a = a * a % mod;
        b /= 2;
    }
    return result;
}

int main() {
    // Предвычисление факториалов
    fact[0] = 1;
    for (int i = 1; i < MAXN; ++i) {
        fact[i] = fact[i - 1] * i % MOD;
    }

    // Предвычисление обратных факториалов по модулю (через теорему Ферма)
    inv_fact[MAXN - 1] = mod_pow(fact[MAXN - 1], MOD - 2, MOD);
    for (int i = MAXN - 2; i >= 0; --i) {
        inv_fact[i] = inv_fact[i + 1] * (i + 1) % MOD;
    }

    // Ввод
    int n, k;
    cin >> n >> k;

    // Проверка и вычисление C(n, k)
    if (k < 0 || k > n) {
        cout << 0 << endl;
    } else {
        long long result = fact[n] * inv_fact[k] % MOD * inv_fact[n - k] % MOD;
        cout << result << endl;
    }

    return 0;
}
