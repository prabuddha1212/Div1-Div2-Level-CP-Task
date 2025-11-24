"""
Brute-force solution for XOR Path Queries on Colored Edges.
This solution is naive and may not run efficiently for large inputs,
but is useful for testing and validation on small cases.
"""

import sys

sys.setrecursionlimit(10**7)
input = sys.stdin.readline


def dfs(node, graph, visited):
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(neighbor, graph, visited)


def main():
    n, q, C = map(int, input().split())
    values = list(map(int, input().split()))
    graph = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        a, b, col = map(int, input().split())
        graph[a].append((b, col))
        graph[b].append((a, col))

    for _ in range(q):
        parts = list(map(int, input().split()))
        u, v, k = parts[0], parts[1], parts[2]
        colors_set = set(parts[3:]) if k > 0 else set()

        # Find simple path from u to v via BFS
        from collections import deque

        parent = [-1] * (n + 1)
        queue = deque([u])
        parent[u] = 0
        while queue:
            cur = queue.popleft()
            if cur == v:
                break
            for nxt, _ in graph[cur]:
                if parent[nxt] == -1:
                    parent[nxt] = cur
                    queue.append(nxt)
        # Retrieve path nodes
        path_nodes = []
        cur = v
        while cur != 0:
            path_nodes.append(cur)
            cur = parent[cur]
        path_nodes.reverse()

        # Build subgraph edges on path with colors in set
        subgraph = {node: [] for node in path_nodes}
        for i in range(len(path_nodes) - 1):
            a = path_nodes[i]
            b = path_nodes[i + 1]
            col = None
            for nb, c in graph[a]:
                if nb == b:
                    col = c
                    break
            if col in colors_set:
                subgraph[a].append(b)
                subgraph[b].append(a)

        # DFS from u in subgraph to find component
        visited = set()
        dfs(u, subgraph, visited)
        result = 0
        for node in visited:
            result ^= values[node - 1]
        print(result)


if __name__ == "__main__":
    main()
