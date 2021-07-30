import math
import os
import random
import re
import sys

def timeConversion(s):
    if 'A' in s:
        if int(s[:2]) == 12:
            s = '00'+s[2:8]
        else:
            s = s[:8]
    
    if 'P' in s:
        if int(s[:2]) == 12:
            s = s[:8]
        else:
            hh = int(s[:2]) + 12
            s = str(hh)+s[2:8]

    return s

if __name__ == '__main__':
    s = '12:05:45PM'
    result = timeConversion(s)
    print(result)