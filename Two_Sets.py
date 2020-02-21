import math
import functools

def great(a,b):
    while not a % b == 0:
        a, b = b, (a%b)
    return b

def least(a,b):
    return a*b // great(a,b)

def getTotalX(a, b):
    low_GCD = functools.reduce(great,b)
    high_LCM = functools.reduce(least,a)
    nums = sum([1 for x in range(high_LCM, low_GCD + 1, high_LCM) if low_GCD % x == 0])
    return nums

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])
    arr = list(map(int, input().rstrip().split()))
    brr = list(map(int, input().rstrip().split()))
    total = getTotalX(arr, brr)
    print(str(total) + '\n')
