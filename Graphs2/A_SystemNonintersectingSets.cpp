#include <iostream>
#include <vector>
#include <string>
using namespace std;

const int MAXN = 300005;

int parent[MAXN];
int size_[MAXN];
int min_[MAXN];
int max_[MAXN];

int find(int v) {
    if (v == parent[v])
        return v;
    return parent[v] = find(parent[v]);
}

void union_sets(int a, int b) {
    a = find(a);
    b = find(b);
    if (a != b) {
        if (size_[a] < size_[b])
            swap(a,b);
        parent[b] = a;
        size_[a] += size_[b];
        min_[a] = std::min(min_[a],min_[b]);
        max_[a] = std::max(max_[a],max_[b]);
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n,m;
    cin >> n >> m;
    for (int i = 1; i <= n; ++i) {
        parent[i] = i;
        size_[i] = 1;
        min_[i] = i;
        max_[i] = i;
    }
    
    while (m--) {
        string cmd;
        int x,y;
        cin >> cmd >> x;
        if (cmd == "union") {
            cin >> y;
            union_sets(x,y);
        } else if (cmd == "get") {
            int r = find(x);
            cout << min_[r] << " " << max_[r] << " " << size_[r] << "\n";
        }
    }
    
    return 0;
}