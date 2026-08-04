class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)

        parent = [i for i in range(n)]
        rank = [1] * n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            rootX = find(x)
            rootY = find(y)

            if rootX == rootY:
                return False

            if rank[rootX] < rank[rootY]:
                parent[rootX] = rootY
                rank[rootY] += rank[rootX]
            else:
                parent[rootY] = rootX
                rank[rootX] += rank[rootY]

            return True

        for u, v in edges:
            if not union(u - 1, v - 1):
                return [u, v]
                