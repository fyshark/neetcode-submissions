class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        for course, pre in prerequisites:
            adj[pre].append(course)
            indegree[course] += 1

        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        
        count = 0
        order = []
        while q:
            curr_node = q.popleft()
            count += 1
            order.append(curr_node)

            for next_node in adj[curr_node]:
                indegree[next_node] -= 1
                if indegree[next_node] == 0:
                    q.append(next_node)
                    
        return order if count == numCourses else []