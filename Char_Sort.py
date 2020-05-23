from collections import Counter
class Solution:
    def frequencySort(self, s):
        rearrangedS = ''
        s = sorted(dict(Counter(s)).items(), key=lambda x:x[1], reverse = True)
        for characters in s:
            rearrangedS += characters[0] * characters[1]
        return(rearrangedS)