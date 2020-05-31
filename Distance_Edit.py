from functools import lru_cache

class Solution:
    def minDistance(self, word1, word2):
        @lru_cache(None)
        def distance(wordOne, wordTwo, lenOne, lenTwo):
            if lenOne == 0:
                return lenTwo
            if lenTwo == 0:
                return lenOne
            if wordOne[lenOne-1] == wordTwo[lenTwo-1]:
                return distance(wordOne, wordTwo, lenOne-1, lenTwo-1)
            return 1 + min(distance(wordOne, wordTwo, lenOne, lenTwo-1), 
                           distance(wordOne, wordTwo, lenOne-1, lenTwo), 
                           distance(wordOne, wordTwo, lenOne-1, lenTwo-1))
        return distance(word1, word2, len(word1), len(word2))