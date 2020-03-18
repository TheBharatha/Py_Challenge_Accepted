class Solution:
    def sortString(self, s: str) -> str:
        s = sorted(s)
        sLen = len(s)
        fwdSort = True
        result = list()
        rem = list()
        rLen = len(result)
        if len(sorted(set(s))) == 1:
            return(''.join(s))
        elif len(s) == len(sorted(set(s))):
            return(''.join(sorted(set(s))))
        else:
            while sLen != 0:
                if fwdSort == True:
                    result.append(s.pop(0))
                    sLen = len(s)
                    for ch in range(sLen):
                        if s[ch] > result[len(result)-1]:
                            result.append(s[ch])
                        else:
                            rem.append(s[ch])
                    fwdSort = False
                    ch = 0
                    s = sorted(rem, reverse = True)
                    sLen = len(rem)
                    rem.clear()
                elif fwdSort == False:
                    result.append(s.pop(0))
                    sLen = len(s)
                    for ch in range(sLen):
                        if s[ch] < result[len(result)-1]:
                            result.append(s[ch])
                        else:
                            rem.append(s[ch])
                    fwdSort = True
                    ch = 0
                    s = sorted(rem)
                    sLen = len(rem)
                    rem.clear()
        return(''.join(result))
