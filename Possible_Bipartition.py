from collections import defaultdict
class Solution:
    def possibleBipartition(self, N, dislikes):
        good, hate, noHate = 0, 1, -1
        
        def group(person, emotion):
            idealGroup[person] = emotion
            for other in hatred[person]:
                if idealGroup[other] == emotion:
                    return False
                if idealGroup[other] == good and (not group(other, -emotion)):
                    return False
            return True
        
        if N == 1 or not dislikes:
            return True
        
        hatred = defaultdict(list)
        idealGroup = [good for _ in range(N+1)]
        
        for one, another in dislikes:
            hatred[one].append(another)
            hatred[another].append(one)
        
        for  person in range(1, N+1):
            if idealGroup[person] == good and (not group(person, hate)):
                return False
        return True