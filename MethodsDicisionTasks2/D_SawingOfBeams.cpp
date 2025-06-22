#include <iostream>
#include <vector>
#include <climits>
using namespace std;

int main() {
    int L, N;
    cin >> L >> N;
    
    vector<int> cuts(N + 2);
    cuts[0] = 0;
    cuts[N + 1] = L;
    
    for (int i = 1; i <= N; ++i) {
        cin >> cuts[i];
    }
    
    vector<vector<int>> dp(N + 2, vector<int>(N + 2, 0));
    
    for (int len = 2; len <= N + 1; ++len) {
        for (int i = 0; i + len <= N + 1; ++i) {
            int j = i + len;
            dp[i][j] = INT_MAX;
            for (int k = i + 1; k < j; ++k) {
                int cost = dp[i][k] + dp[k][j] + cuts[j] - cuts[i];
                dp[i][j] = min(dp[i][j], cost);
            }
        }
    }
    
    cout << dp[0][N + 1] << '\n';
    return 0;
}