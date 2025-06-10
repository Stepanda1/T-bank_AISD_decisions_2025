#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

struct SegmentTree {
    int size;
    vector<ll> sum, add;
    vector<optional<ll>> set;

    SegmentTree(int n) {
        size = 1;
        while (size < n) size <<= 1;
        sum.assign(2 * size, 0);
        add.assign(2 * size, 0);
        set.assign(2 * size, nullopt);
    }

    void apply_set(int x, int lx, int rx, ll v) {
        sum[x] = v * (rx - lx);
        set[x] = v;
        add[x] = 0;
    }

    void apply_add(int x, int lx, int rx, ll v) {
        if (set[x]) {
            set[x] = *set[x] + v;
        } else {
            add[x] += v;
        }
        sum[x] += v * (rx - lx);
    }

    void push(int x, int lx, int rx) {
        if (rx - lx == 1) return;
        int m = (lx + rx) >> 1;
        if (set[x]) {
            apply_set(2*x+1, lx, m, *set[x]);
            apply_set(2*x+2, m, rx, *set[x]);
            set[x] = nullopt;
        }
        if (add[x]) {
            apply_add(2*x+1, lx, m, add[x]);
            apply_add(2*x+2, m, rx, add[x]);
            add[x] = 0;
        }
    }

    void _set(int l, int r, ll v, int x, int lx, int rx) {
        if (r <= lx || rx <= l) return;
        if (l <= lx && rx <= r) {
            apply_set(x, lx, rx, v);
            return;
        }
        push(x, lx, rx);
        int m = (lx + rx) >> 1;
        _set(l, r, v, 2*x+1, lx, m);
        _set(l, r, v, 2*x+2, m, rx);
        sum[x] = sum[2*x+1] + sum[2*x+2];
    }

    void _add(int l, int r, ll v, int x, int lx, int rx) {
        if (r <= lx || rx <= l) return;
        if (l <= lx && rx <= r) {
            apply_add(x, lx, rx, v);
            return;
        }
        push(x, lx, rx);
        int m = (lx + rx) >> 1;
        _add(l, r, v, 2*x+1, lx, m);
        _add(l, r, v, 2*x+2, m, rx);
        sum[x] = sum[2*x+1] + sum[2*x+2];
    }

    ll _sum(int l, int r, int x, int lx, int rx) {
        if (r <= lx || rx <= l) return 0;
        if (l <= lx && rx <= r) return sum[x];
        push(x, lx, rx);
        int m = (lx + rx) >> 1;
        return _sum(l, r, 2*x+1, lx, m) + _sum(l, r, 2*x+2, m, rx);
    }

    void assign(int l, int r, ll v) {
        _set(l, r, v, 0, 0, size);
    }

    void add_val(int l, int r, ll v) {
        _add(l, r, v, 0, 0, size);
    }

    ll range_sum(int l, int r) {
        return _sum(l, r, 0, 0, size);
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    cin >> n >> m;
    SegmentTree tree(n);

    for (int i = 0; i < m; ++i) {
        int type;
        cin >> type;
        if (type == 1) {
            int l, r;
            ll v;
            cin >> l >> r >> v;
            tree.assign(l, r, v);
        } else if (type == 2) {
            int l, r;
            ll v;
            cin >> l >> r >> v;
            tree.add_val(l, r, v);
        } else {
            int l, r;
            cin >> l >> r;
            cout << tree.range_sum(l, r) << '\n';
        }
    }

    return 0;
}
