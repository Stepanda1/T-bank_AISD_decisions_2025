#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>
using namespace std;

const int MAXN = 100005;
const int LOG = 17; // потому что 2^17 > 1e5

vector<pair<int, int>> tree[MAXN]; // (child, cost)
int up[MAXN][LOG];
int minEdge[MAXN][LOG];
int depth[MAXN];

void dfs(int v, int parent, int weight) {
    up[v][0] = parent;
    minEdge[v][0] = weight;
    
    for (int i = 1; i < LOG; ++i) {
        if (up[v][i-1] != -1) {
            up[v][i] = up[up[v][i-1]][i-1];
            minEdge[v][i] = min(minEdge[v][i-1], minEdge[up[v][i-1]][i-1]);
        } else {
            up[v][i] = -1;
            minEdge[v][i] = INT_MAX;
        }
    }
    
    for (auto& edge : tree[v]) {
        int to = edge.first;
        int w = edge.second;
        depth[to] = depth[v] + 1;
        dfs(to, v, w);
    }
}

int getMinEdge(int u, int v) {
    int res = INT_MAX;
    
    if (depth[u] < depth[v])
        swap(u, v);
        
    for (int i = LOG - 1; i >= 0; --i) {
        if (up[u][i] != -1 && depth[up[u][i]] >= depth[v]) {
            res = min(res, minEdge[u][i]);
            u = up[u][i];
        }
    }
    
    if (u == v) return res;
    
    for (int i = LOG - 1; i >= 0; --i) {
        if (up[u][i] != -1 && up[u][i] != up[v][i]) {
            res = min({res, minEdge[u][i], minEdge[v][i]});
            u = up[u][i];
            v = up[v][i];
        }
    }
    
    res = min({res, minEdge[u][0], minEdge[v][0]});
    return res;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n;
    cin >> n;
    for (int i = 1; i < n; ++i) {
        int parent, cost;
        cin >> parent >> cost;
        tree[parent].emplace_back(i, cost);
    }
    
    for (int i = 0; i < n; ++i)
        for (int j = 0; j < LOG; ++j)
            up[i][j] = -1, minEdge[i][j] = INT_MAX;
            
    dfs(0, -1, INT_MAX);
    
    int m;
    cin >> m;
    while (m--) {
        int u,v;
        cin >> u >> v;
        cout << getMinEdge(u, v) << "\n";
    }
    
    return 0;
}