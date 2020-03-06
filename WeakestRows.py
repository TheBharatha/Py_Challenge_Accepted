class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        sums = list()
        weak = list()
        i = 0
        for st in mat:
            sums.append([sum(st),i])
            # i makes up for the address of the sums elements.
            i += 1
        # sums will have the elements like sums[st][i]
        sums.sort()
        sums = sums[:k]
        for wk in sums:
            weak.append(wk[1])
        return(weak)
