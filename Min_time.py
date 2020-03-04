class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        xDiff = yDiff = time = 0
        for i in range(len(points)-1):
        #Get the absolute difference and add the max value between x and y to the time variable
            xDiff = abs(points[i][0] - points[i+1][0])
            yDiff = abs(points[i][1] - points[i+1][1])
            time = time + max(xDiff, yDiff)
        return time
