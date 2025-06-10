#include <bits/stdc++.h>
using namespace std;

using Interval = pair<int, int>;
set<Interval> black;
long long totalLength = 0;

void add_black(int l, int r) {
    auto it = black.lower_bound({l, l});
    if (it != black.begin()) --it;

    vector<Interval> to_erase;
    int new_l = l, new_r = r;

    while (it != black.end() && it->first <= r) {
        if (it->second < l) {
            ++it;
            continue;
        }
        // объединяем
        new_l = min(new_l, it->first);
        new_r = max(new_r, it->second);
        totalLength -= it->second - it->first;
        to_erase.push_back(*it);
        ++it;
    }

    for (auto& seg : to_erase) black.erase(seg);
    black.insert({new_l, new_r});
    totalLength += new_r - new_l;
}

void remove_black(int l, int r) {
    auto it = black.lower_bound({l, l});
    if (it != black.begin()) --it;

    vector<Interval> to_erase, to_add;

    while (it != black.end() && it->first < r) {
        int a = it->first, b = it->second;
        if (b <= l) {
            ++it;
            continue;
        }
        to_erase.push_back(*it);
        totalLength -= b - a;
        if (a < l) to_add.push_back({a, l});
        if (r < b) to_add.push_back({r, b});
        ++it;
    }

    for (auto& seg : to_erase) black.erase(seg);
    for (auto& seg : to_add) {
        black.insert(seg);
        totalLength += seg.second - seg.first;
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;

    while (n--) {
        char c;
        int x, l;
        cin >> c >> x >> l;
        int left = x, right = x + l;

        if (c == 'B') {
            add_black(left, right);
        } else {
            remove_black(left, right);
        }

        cout << black.size() << ' ' << totalLength << '\n';
    }

    return 0;
}