#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main() {
    string s;
    cin >> s;
    int n = s.size();

    vector<vector<int>> dp(n, vector<int>(n, 0));

    // Длина 1 — это палиндром
    for (int i = 0; i < n; ++i)
        dp[i][i] = 1;

    // Построение dp
    for (int len = 2; len <= n; ++len) {
        for (int i = 0; i + len - 1 < n; ++i) {
            int j = i + len - 1;
            if (s[i] == s[j]) {
                dp[i][j] = (len == 2 ? 2 : dp[i + 1][j - 1] + 2);
            } else {
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1]);
            }
        }
    }

    // Восстановление палиндрома
    string res;
    int i = 0, j = n - 1;
    string left = "", right = "";

    while (i <= j) {
        if (s[i] == s[j]) {
            if (i == j)
                left += s[i]; // середина
            else {
                left += s[i];
                right = s[j] + right;
            }
            ++i;
            --j;
        } else if (dp[i + 1][j] > dp[i][j - 1]) {
            ++i;
        } else {
            --j;
        }
    }

    res = left + right;
    cout << res.size() << '\n';
    cout << res << '\n';

    return 0;
}
