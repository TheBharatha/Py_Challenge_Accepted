import math
import os
import sys

def migratoryBirds(arr):
    arr.sort()
    FFB = my_bird = count = 0
    for bird in range(len(arr)-1):
        if arr[bird] == arr[bird+1]:
            count += 1
            if count > my_bird:
                my_bird = count
                FFB = arr[bird]
        else:
            count = 0
    return(FFB)


if __name__ == '__main__':
    arr_count = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    result = migratoryBirds(arr)
    print(str(result) + '\n')
