"""
Random test case generator for XOR Path Queries on Colored Edges problem.
Generates random trees and queries within given constraints.
"""

import random


def generate_tree(n):
    edges = []
    for i in range(2, n + 1):
        parent = random.randint(1, i - 1)
        edges.append((parent, i))
    return edges


def generate():
    n = 1000
    q = 100
    C = 10
    print(n, q, C)
    values = [random.randint(0, 2**30 - 1) for _ in range(n)]
    print(*values)
    edges = generate_tree(n)
    colors = [random.randint(1, C) for _ in range(n - 1)]
    for i in range(n - 1):
        a, b = edges[i]
        print(a, b, colors[i])
    for _ in range(q):
        u = random.randint(1, n)
        v = random.randint(1, n)
        k = random.randint(0, C)
        subset = random.sample(range(1, C + 1), k)
        print(u, v, k, *subset)


if __name__ == "__main__":
    generate()
