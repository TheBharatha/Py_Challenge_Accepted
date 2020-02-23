import math
import os
import sys

def sockMerchant(n, ar):
    unique = list()
    stock = list()
    pairs = 0
    
    for pair in ar:
        if pair not in unique:
            unique.append(pair)
    
    for color in unique:
        stock.append(ar.count(color))
    
    for stocks in stock:
        pairs = pairs + (stocks//2)
    
    return pairs

if __name__ == '__main__':
    n = int(input())
    ar = list(map(int, input().rstrip().split()))
    result = sockMerchant(n, ar)
    print(str(result) + '\n')
