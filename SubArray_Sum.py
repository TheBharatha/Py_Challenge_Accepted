def arrSum(arr,k):
    subSum = 0
    pos = 0
    while pos <= len(arr) - 2:
        stop = True
        move = pos + 2
        while stop:
            if sum(arr[pos:move]) == k:
                subSum += 1
                stop = False
            if sum(arr[pos:move]) > k:
                stop = False
            move += 1
        pos += 1
    print(subSum)


if __name__ == "__main__":
    arr = [1,1,1]
    k = 2
    arrSum(arr,k)