class Solution:
    def removeDuplicates(self, S: str) -> str:
        uniS = list()
        uniS.append('#')
        for ch in S:
            if ch == uniS[-1]:
                uniS.pop()
            else:
                uniS.append(ch)
        return(''.join(uniS[1:
