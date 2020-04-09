import math
n = 5
k = 3
arr = [4,2]
specialProblems = startPage = 0
currentPage = problemNo = 1
for chapter in arr:
    numberOfPages = math.ceil(chapter/k)
    while problemNo <= chapter:
        #print('Page no', currentPage, 'Problem No: ', problemNo)
        if currentPage == problemNo:
            specialProblems += 1
        if problemNo % k == 0:
            currentPage += 1
        problemNo += 1
    if currentPage == startPage + numberOfPages:
        currentPage += 1
    startPage = currentPage - 1
    problemNo = 1
print(specialProblems)
    
'''
startPage = 0
specialProblems = 0
problemNo = 1
chapter = 1
currentPage = 1
while chapter <= n:
    print('Chapter: ', chapter)
    numberOfPages = math.ceil(arr[chapter-1]/k)
    while currentPage <= startPage + numberOfPages:
        while problemNo <= arr[chapter-1]:
            print('Page no:', currentPage, 'Problem No: ', problemNo)
            if problemNo % k == 0:
                currentPage  += 1
                print('Turned to page: ', currentPage)
                problemNo += 1
        currentPage += 1
    problemNo = 1
    startPage = currentPage - 1
    chapter += 1
'''