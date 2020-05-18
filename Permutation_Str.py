from collections import Counter 
class Solution:
    def checkInclusion(self, s1, s2):
        permutation = ''
        s1Counter = Counter(s1)
        for combo in range(0, len(s2)-len(s1)+1):
            permutation = s2[combo : combo + len(s1)]
            if Counter(permutation) == s1Counter:
                return True
        return False