class Solution:
    def kClosest(self, points, K):
        return sorted(points, key = lambda point: pow(point[0],2) + pow(point[1],2))[:K]
        