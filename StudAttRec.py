class Solution:
    def checkRecord(self, s: str) -> bool:
        reward = True
        if s.count('A') > 1 or 'LLL' in s:
            reward = False
        return(reward)
