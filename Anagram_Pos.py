class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        anagramPositions = list()
        pLen = len(p)
        p = ''.join(sorted(p))
        maxLen = len(s) - pLen
        section = 0
        while section <= maxLen:
            if s[section] in p:
                subS = ''.join(sorted(s[section:pLen]))
                if p in subS:
                    anagramPositions.append(section)
            section += 1
            pLen += 1
        return(anagramPositions)