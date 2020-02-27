class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        countSJ = 0
        for jewel in J:
            countSJ = countSJ + S.count(jewel)
        return countSJ
