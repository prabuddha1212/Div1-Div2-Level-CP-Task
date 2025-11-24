import sys

sys.setrecursionlimit(10**7)
input = sys.stdin.readline


class DSU:
    def __init__(self, n, values):
        self.parent = list(range(n))
        self.size = [1] * n
        self.xor_val = values[:]  # xor of component

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, x, y):
        xroot = self.find(x)
        yroot = self.find(y)
        if xroot == yroot:
            return
        if self.size[xroot] < self.size[yroot]:
            xroot, yroot = yroot, xroot
        self.parent[yroot] = xroot
        self.size[xroot] += self.size[yroot]
        self.xor_val[xroot] ^= self.xor_val[yroot]


def dfs_lca(u, p, adj, depth, up):
    for v, c in adj[u]:
        if v == p:
            continue
        depth[v] = depth[u] + 1
        up[0][v] = u
        dfs_lca(v, u, adj, depth, up)


def build_lca(n, adj):
    LOG = 20
    up = [[0] * (n + 1) for _ in range(LOG)]
    depth = [0] * (n + 1)
    dfs_lca(1, -1, adj, depth, up)
    for i in range(1, LOG):
        for v in range(1, n + 1):
            up[i][v] = up[i - 1][up[i - 1][v]]
    return up, depth


def lca(u, v, up, depth):
    if depth[u] < depth[v]:
        u, v = v, u
    LOG = len(up)
    for i in reversed(range(LOG)):
        if depth[up[i][u]] >= depth[v]:
            u = up[i][u]
    if u == v:
        return u
    for i in reversed(range(LOG)):
        if up[i][u] != up[i][v]:
            u = up[i][u]
            v = up[i][v]
    return up[0][u]


def get_path_edges(u, v, up, depth):
    l = lca(u, v, up, depth)
    edges = []

    def climb(x, stop):
        while x != stop:
            p = up[0][x]
            edges.append((p, x))
            x = p

    climb(u, l)
    climb(v, l)
    return edges


def main():
    n, q, c = map(int, input().split())
    values = list(map(int, input().split()))
    adj = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        a, b, col = map(int, input().split())
        adj[a].append((b, col))
        adj[b].append((a, col))
    up, depth = build_lca(n, adj)
    edges_color = dict()
    for u in range(1, n + 1):
        for v, col in adj[u]:
            key = (u, v) if u < v else (v, u)
            edges_color[key] = col
    for _ in range(q):
        parts = list(map(int, input().split()))
        u, v, k = parts[0], parts[1], parts[2]
        colors = set(parts[3:]) if k > 0 else set()

        path_edges = get_path_edges(u, v, up, depth)
        dsu = DSU(n, values[:])
        for a, b in path_edges:
            key = (a, b) if a < b else (b, a)
            if edges_color.get(key, None) in colors:
                dsu.union(a - 1, b - 1)

        l = lca(u, v, up, depth)

        def climb_nodes(x, stop):
            res = []
            while x != stop:
                res.append(x - 1)
                x = up[0][x]
            res.append(stop - 1)
            return res

        path_nodes = climb_nodes(u, l) + climb_nodes(v, l)[:-1][::-1]
        uroot = dsu.find(u - 1)
        ans = 0
        for node in path_nodes:
            if dsu.find(node) == uroot:
                ans ^= values[node]
        print(ans)


if __name__ == "__main__":
    main()
