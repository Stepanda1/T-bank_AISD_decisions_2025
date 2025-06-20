#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Edge {
    int u,v,w;
    bool operator<(const Edge &other) const {
        return w < other.w;
    }
};

vector<int> parent, rank_set;

int find_set(int v) {
    if (v == parent[v])
        return v;
    return parent[v] = find_set(parent[v]);
}

bool union_sets(int a, int b) {
    a = find_set(a);
    b = find_set(b);
    if (a == b) return false;
    if (rank_set[a] < rank_set[b])
        swap(a,b);
    parent[b] = a;
    if (rank_set[a] == rank_set[b])
        rank_set[a]++;
    return true;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n,m;
    cin >> n >> m;
    
    vector<Edge> edges(m);
    for (int i = 0; i < m; ++i) {
        cin >> edges[i].u >> edges[i].v >> edges[i].w;
    }
    
    sort(edges.begin(), edges.end());
    
    parent.resize(n+1);
    rank_set.resize(n+1);
    for (int i = 1; i <= n; ++i) {
        parent[i] = i;
        rank_set[i] = 0;
    }
    
    long long mst_weight = 0;
    for (const Edge &e : edges) {
        if (union_sets(e.u, e.v)) {
            mst_weight += e.w;
        }
    }
    
    cout << mst_weight << "\n";
    return 0;
}