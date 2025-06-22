#include <iostream>
#include <vector>
#include <string>
using namespace std;

bool isRepeated(const string& s, int l, int r, int len) {
    int n = r - l + 1;
    if (n % len != 0) return false;
    string pattern = s.substr(l, len);
    for (int i = l; i <= r; i += len) {
        if (s.substr(i, len) != pattern)
            return false;
    }
    return true;
}

int main() {
    string s;
    cin >> s;
    int n = s.size();
    vector<vector<string>> dp(n, vector<string>(n));
    
    for (int len = 1; len <= n; ++len) {
        for (int i = 0; i + len - 1 < n; ++i) {
            int j = i + len - 1;
            dp[i][j] = s.substr(i, len);
            
            for (int k = i; k < j; ++k) {
                if (dp[i][j].size() > dp[i][k].size() + dp[k + 1][j].size())
                    dp[i][j] = dp[i][k] + dp[k + 1][j];
            }
            
            for (int l = 1; l <= len / 2; ++l) {
                if (isRepeated(s,i,j,l)) {
                    int times = len / l;
                    string compressed = to_string(times) + "(" + dp[i][i + l - 1] + ")";
                    if (compressed.size() < dp[i][j].size())
                        dp[i][j] = compressed;
                }
            }
        }
    }
    
    cout << dp[0][n - 1] << endl;
    return 0;
}