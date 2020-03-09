class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        i = 0
        j = len(arr)-2
        while i <= j:
            if arr[i] == 0:
                arr.insert(i+1,0)
                arr.pop()
                i += 2
            elif arr[i] != 0:
                i += 1
