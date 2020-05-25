class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        aLen, bLen = len(A), len(B)
        uncrossed = list([0]*(bLen + 1) for _ in range(aLen + 1))
        for a in range(aLen):
            for b in range(bLen):
                uncrossed[a+1][b+1] = max(uncrossed[a][b+1], uncrossed[a+1][b])
                if A[a] == B[b]:
                    uncrossed[a+1][b+1] = max(uncrossed[a+1][b+1], 1 + uncrossed[a][b])
        return uncrossed[-1][-1]
