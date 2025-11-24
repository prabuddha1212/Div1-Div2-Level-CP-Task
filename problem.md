# Problem: XOR Path Queries on Colored Edges

You are given a tree with \( N \) nodes numbered from 1 to \( N \). Each edge of the tree is colored with one of \( C \) colors. Additionally, each node \( i \) has an associated integer value \( v_i \).

Your task is to answer \( Q \) queries. Each query is described by two nodes \( u \) and \( v \), and a subset of colors \( S \subseteq \{1, 2, \ldots, C\} \). For each query, consider the unique simple path from \( u \) to \( v \) in the tree. The path consists of edges and nodes. We only consider those edges whose color is in subset \( S \). The path is restricted to edges with colors in \( S \). Find the XOR of the values of all nodes on the connected component of \( u \) in this restricted path to \( v \).

More formally:

- Construct a subgraph \( G' \) of the original tree where edges whose color is not in \( S \) are removed.
- Let \( P \) be the simple path from \( u \) to \( v \) in the original tree.
- Find the connected component containing \( u \) in the subgraph induced by edges in \( S \) intersecting path \( P \).
- Compute the XOR of the values of all nodes in this connected component.

If \( v \) is not reachable from \( u \) using edges colored in \( S \), output the XOR of the values of nodes reachable from \( u \) via edges in \( S \) restricted to the path \( P \).

---

### Input

- The first line contains three integers \( N \), \( Q \), and \( C \) \((1 \leq N, Q \leq 100\,000, 1 \leq C \leq 20)\) — the number of nodes, queries, and colors respectively.
- The second line contains \( N \) integers \( v_1, v_2, \ldots, v_N \) \((0 \leq v_i < 2^{30})\) — the values of the nodes.
- Then \( N-1 \) lines follow, each describing an edge with three integers \( a \), \( b \), and \( col \) \((1 \leq a,b \leq N, 1 \leq col \leq C)\) — representing an edge between nodes \( a \) and \( b \) with color \( col \).
- Then \( Q \) lines follow, each describing a query:
  - The first integer \( u \) \((1 \leq u \leq N)\),
  - The second integer \( v \) \((1 \leq v \leq N)\),
  - The third integer \( k \) \((0 \leq k \leq C)\) — the number of colors in subset \( S \),
  - Followed by \( k \) distinct integers denoting the colors in \( S \).

---

### Output

For each query, output a single integer — the XOR of the values of nodes in the connected component of \( u \) within the path \( P \) restricted to edges with colors in \( S \).

---

### Example

**Input**

```
5 3 3
1 2 3 4 5
1 2 1
2 3 2
3 4 1
4 5 3
1 5 2 1 3
2 5 1 2
1 3 0
```

**Output**

```
15
5
1
```

### Explanation

- Query 1: subset \( S = \{1, 3\} \). The path from 1 to 5 is 1—2—3—4—5. Using only edges with colors 1 or 3, edges (1-2), (3-4), and (4-5) are included. Connected to 1 are nodes 1,2 and 3,4,5 is disconnected from 2 since edge (2-3) has color 2 not in \( S \). The XOR is \(1 \oplus 2 \oplus 3 \oplus 4 \oplus 5=15\).
- Query 2: \( S = \{2\} \). Path from 2 to 5 is 2—3—4—5. Using only edges colored 2, edge (2-3) included, connected component of 2 includes nodes 2 and 3 only. XOR = 2 \oplus 3 = 1.
- Query 3: \( S = \emptyset \). No edges included, so only \( u=1 \) is connected. XOR = 1.

---

### Constraints

- \( 1 \leq N, Q \leq 10^5 \)
- \( 1 \leq C \leq 20 \)
- \( 0 \leq v_i < 2^{30} \)

---

### Note

Efficient solutions require careful data structures and bitmasking over colors. Brute-force will not pass time limits.
