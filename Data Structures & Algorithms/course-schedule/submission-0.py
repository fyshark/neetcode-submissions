class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        vis = [False] * numCourses
        path = [False] * numCourses
        for course, pre in prerequisites:
            adj[pre].append(course)
        
        def dfs(node):
            path[node] = vis[node] = True
            for next_node in adj[node]:
                if not vis[next_node]:
                    if dfs(next_node): return True
                elif path[next_node]: return True
            path[node] = False
            return False
        
        for i in range(numCourses):
            if not vis[i]:
                if dfs(i):
                    return False
        return True