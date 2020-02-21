def breakingRecords(scores):
    high = low = scores[0]
    breakHigh = breakLow = 0
    for score in range(1,len(scores)):
        if scores[score] > high:
            breakHigh += 1
            high = scores[score]
        elif scores[score] < low:
            breakLow += 1
            low = scores[score]
    return(breakHigh,breakLow)

if __name__ == '__main__':
    n = int(input())
    scores = list(map(int, input().rstrip().split()))
    result = breakingRecords(scores)
    print(' '.join(map(str, result)))
