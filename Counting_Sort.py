import math

class CountSort:
    def countingSort(self, arr):
        self.arr = arr
        indexList = list(range(0,len(arr)))
        countList = list(map(self.giveIndex,indexList))
        return(countList)
    
    def giveIndex(self, ele):
        counts = self.arr.count(ele)
        return(counts)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    countSort = CountSort()
    result = countSort.countingSort(arr)
    print(' '.join(map(str, result)))
    print('\n')