import math

def workbook(n, k, arr):
    chapterCount = specialProblems = startPage = 0
    currentPage = problemNo = 1
    for chapter in arr:
        chapterCount += 1
        print('\n Chapter: ', chapterCount)
        numberOfPages = math.ceil(chapter/k)
        print('Number of pages required for ', chapter, 'problem/s are/is ', numberOfPages)
        while problemNo <= chapter:
            print('Page no: ', currentPage, ', Problem index: ', problemNo)
            if currentPage == problemNo:
                print('Special problem match found at page ', currentPage, 'for problem ', problemNo)
                specialProblems += 1
            if problemNo % k == 0:
                currentPage += 1
                print('Max number of problems per page reached! moving to page', currentPage)
            problemNo += 1
        if currentPage == startPage + numberOfPages:
            currentPage += 1
            print('Visited all the problems in chapter', chapterCount, 'moving to page', currentPage)
        startPage = currentPage - 1
        problemNo = 1
    return(specialProblems)

if __name__ == '__main__':

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = workbook(n, k, arr)

    print('\n Total number of special problems in the workbook are ', str(result))