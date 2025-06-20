#include <iostream>
#include <vector>
#include <queue>
#include <limits>
using namespace std;

const int INF = numeric_limits<int>::max();

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    cin >> n >> m;

    vector<vector<pair<int, int>>> graph(n);  // graph[u] = {v, weight}

    for (int i = 0; i < m; ++i) {
        int u, v, w;
        cin >> u >> v >> w;
        --u; --v;  // к 0-индексации
        graph[u].push_back(make_pair(v, w));
        graph[v].push_back(make_pair(u, w));  // неориентированный
    }

    vector<int> dist(n, INF);
    dist[0] = 0;

    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
    pq.push(make_pair(0, 0));  // {расстояние, вершина}

    while (!pq.empty()) {
        pair<int, int> top = pq.top();
        pq.pop();
        int cur_dist = top.first;
        int u = top.second;

        if (cur_dist > dist[u]) continue;

        for (size_t i = 0; i < graph[u].size(); ++i) {
            int v = graph[u][i].first;
            int weight = graph[u][i].second;
            if (dist[v] > dist[u] + weight) {
                dist[v] = dist[u] + weight;
                pq.push(make_pair(dist[v], v));
            }
        }
    }

    for (int i = 0; i < n; ++i)
        cout << dist[i] << " ";
    cout << "\n";

    return 0;
}