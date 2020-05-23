class Solution:
    def intervalIntersection(self, A, B):
        aLen = len(A)
        bLen = len(B)
        start = 0
        end = 0
        intersections = list()
        while start < aLen and end < bLen:
            lowRange = max(A[start][0], B[end][0])
            highRange = min(A[start][1], B[end][1])
            if lowRange <= highRange:
                intersections.append([lowRange, highRange])
            if A[start][1] < B[end][1]:
                start += 1
            else:
                end += 1
        return intersections