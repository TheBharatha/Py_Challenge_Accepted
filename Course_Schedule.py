class Solution:
    def canFinish(self, numCourses, prerequisites):
        neighbor = [[] for x in range(numCourses)]
        
        for course, prereq in prerequisites:
            neighbor[prereq].append(course)
        
        for source in range(numCourses):
            visited = [False for x in range(numCourses)]
            s = [source]
            while len(s):
                temp = s.pop()
                if not visited[temp]:
                    s.extend(neighbor[temp])
                elif temp == source:
                    return False
                visited[temp] = True
        return True