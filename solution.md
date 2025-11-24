# Solution Explanation for "XOR Path Queries on Colored Edges"

## Problem Restatement

Given a tree of \( N \) nodes with edges colored from a set of \( C \) colors, and each node having a value, we need to answer queries that ask for the XOR of node values reachable from node \( u \) on the path to node \( v \), considering only edges whose colors belong to a subset \( S \).

## Key Observations

- The problem reduces to finding XORs of nodes in the connected component of \( u \) in the subgraph formed by edges in color subset \( S \) restricted to the path \( P \) from \( u \) to \( v \).
- Since the graph is a tree, the path \( P \) is unique.
- The subgraph induced by \( S \) edges may disconnect the path into multiple components.
- Node \( u \) is always included; we want to XOR node values reachable under the given constraints.

## Data Structures and Techniques

1. **Heavy-Light Decomposition (HLD):**

   - Used to split the tree into chains such that path queries can be answered by jumping along chains in \( O(\log N) \).
   - Stores preorder traversal indices for segment tree queries.

2. **Segment Trees:**

   - One segment tree per color (since \( C \leq 20 \)), storing XOR of node values at positions representing edges of that color.
   - This allows efficient XOR queries restricted to edges of each color.

## Algorithm Steps

- For each node (except root), assign the color of the edge connecting it to its parent.
- Build one segment tree per color. In these trees, store node values at positions determined by the HLD index if the parent edge has that color.
- For each query, the subset \( S \) is the set of colors to include.
- Using HLD, split the path from \( u \) to \( v \) into multiple chain segments.
- For each chain segment, query the segment trees for colors in \( S \) and XOR their results.
- Include the value of node \( u \) itself (since node is always reachable from itself).
- Output the final XOR result.

## Complexity

- Building HLD: \( O(N) \)
- Building segment trees: \( O(C \times N) \)
- Each query: \( O(C \times \log N) \) since each color segment tree is queried independently for \( O(\log N) \) segments.
- Overall efficient for up to \( 10^5 \) nodes and queries.

## Conclusion

The solution effectively combines tree decomposition and bitmask-filtered segment tree queries to solve complex edge color filtering and connectivity queries on a tree path in optimal time.
