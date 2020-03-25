class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        result = ''
        openB = closeB = start = 0
        for bracket in range(len(S)):
            if S[bracket] == '(':
                openB += 1
            else:
                closeB += 1
            if openB == closeB:
                end = bracket
                if S[start:end] != '()':
                    result = result + (S[start+1:end])
                    openB = closeB = 0
                    start = bracket + 1
        return(result)
