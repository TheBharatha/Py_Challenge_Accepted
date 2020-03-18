class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for num in range(len(arr)-1):
            arr[num] = max(arr[num+1:])
        arr[len(arr)-1] = -1    
        return(arr)
