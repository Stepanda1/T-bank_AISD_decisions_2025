#include <iostream>
#include <vector>
#include <queue>
#include <limits>
#include <tuple>

using namespace std;

const int INF = numeric_limits<int>::max();
const int64_t TRUCK_WEIGHT = 3000000;
const int64_t CUP_WEIGHT = 100;
const int MAX_TIME = 1440;

struct Edge {
    int to;
    int time;
    int64_t max_weight;
};

int N, M;
vector<vector<Edge>> graph;

bool can_deliver(int64_t cups) {
    int64_t total_weight = TRUCK_WEIGHT + cups * CUP_WEIGHT;
    vector<int> dist(N + 1, INF);
    dist[1] = 0;
    
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
    pq.push(make_pair(0, 1));
    
    while (!pq.empty()) {
        pair<int, int> top = pq.top();
        pq.pop();
        int time_u = top.first;
        int u = top.second;
        
        if (time_u > dist[u]) continue;
        
        for (size_t i = 0; i < graph[u].size(); ++i) {
            Edge e = graph[u][i];
            if (e.max_weight < total_weight) continue;
            
            int v = e.to;
            int new_time = dist[u] + e.time;
            
            if (new_time < dist[v]) {
                dist[v] = new_time;
                pq.push(make_pair(new_time, v));
            }
        }
    }
    
    return dist[N] <= MAX_TIME;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    cin >> N >> M;
    graph.resize(N + 1);
    
    for (int i = 0; i < M; ++i) {
        int u, v, t;
        int64_t w;
        cin >> u >> v >> t >> w;
        graph[u].push_back({v, t, w});
        graph[v].push_back({u, t, w});
    }
    
    int64_t left = 0, right = 100000000;
    int64_t answer = 0;
    
    while(left <= right) {
        int64_t mid = (left + right) / 2;
        if (can_deliver(mid)) {
            answer = mid;
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    
    cout << answer << "\n";
    return 0;
}