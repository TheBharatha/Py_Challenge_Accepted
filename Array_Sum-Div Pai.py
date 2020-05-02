import math
import os
import re
import sys

def divisibleSumPairs(n, k, ar):
    b = ar
    count = 0
    for i in range(n-1):
        for j in range(i+1,n):
            if (ar[i]+b[j]) % k == 0:
                    count += 1
    return count

if __name__ == '__main__':
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    ar = list(map(int, input().rstrip().split()))
    result = divisibleSumPairs(n, k, ar)
    print(str(result) + '\n')