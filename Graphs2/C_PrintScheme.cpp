#include <iostream>
#include <vector>
#include <tuple>
#include <algorithm>
using namespace std;

const int MAX = 105;

int n, m;
int grid[MAX][MAX];
pair<int, int> parent[MAX][MAX];

pair<int, int> find(pair<int, int> u) {
    if (parent[u.first][u.second] != u)
        parent[u.first][u.second] = find(parent[u.first][u.second]);
    return parent[u.first][u.second];
}

bool unite(pair<int, int> u, pair<int, int> v) {
    pair<int, int> pu = find(u), pv = find(v);
    if (pu == pv) return false;
    parent[pu.first][pu.second] = pv;
    return true;
}

int main() {
    cin >> n >> m;

    for (int i = 0; i < n; ++i)
        for (int j = 0; j < m; ++j)
            cin >> grid[i][j];

    for (int i = 0; i < n; ++i)
        for (int j = 0; j < m; ++j)
            parent[i][j] = make_pair(i, j);

    for (int i = 0; i < n; ++i)
        for (int j = 0; j < m; ++j) {
            int code = grid[i][j];
            if ((code & 1) && i + 1 < n)
                unite(make_pair(i, j), make_pair(i + 1, j));
            if ((code & 2) && j + 1 < m)
                unite(make_pair(i, j), make_pair(i, j + 1));
        }

    vector<tuple<int, int, int, int>> edges;

    for (int i = 0; i < n; ++i)
        for (int j = 0; j < m; ++j) {
            int code = grid[i][j];
    
            if (i + 1 < n && !(code & 1)) // если нет вертикальной перемычки
                edges.push_back(make_tuple(1, i, j, 1));
    
            if (j + 1 < m && !(code & 2)) // если нет горизонтальной перемычки
                edges.push_back(make_tuple(2, i, j, 2));
        }


    sort(edges.begin(), edges.end());

    int total_cost = 0;
    vector<tuple<int, int, int>> result;

    for (size_t idx = 0; idx < edges.size(); ++idx) {
        int cost = get<0>(edges[idx]);
        int i = get<1>(edges[idx]);
        int j = get<2>(edges[idx]);
        int d = get<3>(edges[idx]);

        pair<int, int> u = make_pair(i, j);
        pair<int, int> v = (d == 1) ? make_pair(i + 1, j) : make_pair(i, j + 1);

        if (unite(u, v)) {
            result.push_back(make_tuple(i + 1, j + 1, d));
            total_cost += cost;
        }
    }

    cout << result.size() << " " << total_cost << "\n";
    for (size_t i = 0; i < result.size(); ++i)
        cout << get<0>(result[i]) << " " << get<1>(result[i]) << " " << get<2>(result[i]) << "\n";

    return 0;
}