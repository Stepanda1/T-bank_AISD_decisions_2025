#include <iostream>
#include <vector>
#include <queue>
#include <limits>
using namespace std;

typedef long long ll;
const ll INF = numeric_limits<ll>::max();

int n, m;
vector<vector<pair<int, int>>> graph;

vector<ll> dijkstra(int start) {
    vector<ll> dist(n + 1, INF);
    dist[start] = 0;
    priority_queue<pair<ll, int>, vector<pair<ll, int>>, greater<>> pq;
    pq.emplace(0, start);
    
    while (!pq.empty()) {
        ll cur_dist = pq.top().first;
        int u = pq.top().second;
        pq.pop();
        
        if (cur_dist > dist[u]) continue;
        
        for (auto &edge : graph[u]) {
            int v = edge.first;
            int w = edge.second;
            if (dist[v] > dist[u] + w) {
                dist[v] = dist[u] + w;
                pq.emplace(dist[v], v);
            }
        }
    }
    return dist;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    cin >> n >> m;
    graph.resize(n + 1);
    
    for (int i = 0; i < m; ++i) {
        int u, v, w;
        cin >> u >> v >> w;
        graph[u].emplace_back(v, w);
        graph[v].emplace_back(u, w);
    }
    
    int a, b, c;
    cin >> a >> b >> c;
    
    vector<ll> da = dijkstra(a);
    vector<ll> db = dijkstra(b);
    vector<ll> dc = dijkstra(c);
    
    ll ab = da[b], ac = da[c];
    ll ba = db[a], bc = db[c];
    ll ca = dc[a], cb = dc[b];
    
    ll res = INF;
    if (ab != INF && bc != INF) res = min(res, ab + bc);
    if (ac != INF && cb != INF) res = min(res, ac + cb);
    if (ba != INF && ac != INF) res = min(res, ba + ac);
    if (bc != INF && ca != INF) res = min(res, bc + ca);
    if (ca != INF && ab != INF) res = min(res, ca + ab);
    if (cb != INF && ba != INF) res = min(res, cb + ba);
    
    cout << (res == INF ? -1 : res) << "\n";
    return 0;
}