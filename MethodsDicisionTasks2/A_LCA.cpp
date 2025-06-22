#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

const int MAXN = 100005;
const int LOG = 17;

vector<int> tree[MAXN];
int up[MAXN][LOG];
int depth[MAXN];

void dfs(int v, int parent) {
    up[v][0] = parent;
    for (int i = 1; i < LOG; ++i) {
        if (up[v][i-1] != -1)
            up[v][i] = up[up[v][i-1]][i-1];
        else
            up[v][i] = -1;
    }
    for (int to : tree[v]) {
        depth[to] = depth[v] + 1;
        dfs(to, v);
    }
}

int lca(int u, int v) {
    if (depth[u] < depth[v])
        swap(u, v);
        
    for (int i = LOG - 1; i >= 0; --i) {
        if (up[u][i] != -1 && depth[up[u][i]] >= depth[v])
            u = up[u][i];
    }
    if (u == v)
        return u;
    
    for (int i = LOG - 1; i >= 0; --i) {
        if (up[u][i] != -1 && up[u][i] != up[v][i]) {
            u = up[u][i];
            v = up[v][i];
        }
    }
    return up[u][0];
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n;
    cin >> n;
    for (int i = 1; i < n; ++i) {
        int parent;
        cin >> parent;
        tree[parent].push_back(i);
    }
    
    for (int i = 0; i < n; ++i)
        for (int j = 0; j < LOG; ++j)
            up[i][j] = -1;
            
    dfs(0, -1);
    
    int m;
    cin >> m;
    while (m--) {
        int u, v;
        cin >> u >> v;
        cout << lca(u, v) << "\n";
    }
    
    return 0;
}