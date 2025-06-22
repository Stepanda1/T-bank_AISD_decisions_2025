#include <iostream>
#include <vector>
#include <climits>
using namespace std;

int main() {
    long long N;
    int M;
    cin >> N >> M;
    
    vector<long long> A(M);
    long long totalSum = 0;
    
    for (int i = 0; i < M; ++i) {
        cin >> A[i];
        totalSum += A[i] * 2;
    }
    
    if (totalSum < N) {
        cout << -1 << endl;
        return 0;
    }
    
    int bestCount = INT_MAX;
    vector<long long> bestCoins;
    
    int totalComb = 1;
    for (int i = 0; i < M; ++i) totalComb *= 3;
    
    for (int mask = 0; mask < totalComb; ++mask) {
        int temp = mask;
        long long sum = 0;
        int coinCount = 0;
        vector<long long> coins;
        
        for (int i = 0; i < M; ++i) {
            int count = temp % 3;
            temp /= 3;
            sum += A[i] * count;
            coinCount += count;
            for (int j = 0; j < count; ++j)
                coins.push_back(A[i]);
        }
        
        if (sum == N) {
            if (coinCount < bestCount) {
                bestCount = coinCount;
                bestCoins = coins;
            }
        }
    }
    
    if (bestCount == INT_MAX)
        cout << 0 << endl;
    else {
        cout << bestCount << endl;
        for (long long coin : bestCoins)
            cout << coin << ' ';
        cout << endl;
    }
    
    return 0;
}