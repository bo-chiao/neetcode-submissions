class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        remaining = set(range(n))

        adj = defaultdict(list)
        for v1, v2 in edges:
            adj[v1].append(v2)
            adj[v2].append(v1)

        def dfs(node):
            remaining.remove(node)
            
            for neighbor in adj[node]:
                if neighbor in remaining:   
                    dfs(neighbor)

        count = 0
        for i in range(n):
            if i not in remaining:
                continue

            count += 1

            dfs(i)
        
        return count
