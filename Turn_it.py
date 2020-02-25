import os

def pageCount(n, p):
    front = back = 0

    if n%2 == 0 and p%2 != 0:
        front = abs(1-p)//2
        back = ((n-p)//2)+1
    elif n%2 == 0 and p%2 == 0:
        front = (abs(1-p)//2)+1
        back = ((n-p)//2)
    elif n%2 != 0 and p%2 == 0:
        front = (abs(1-p)//2)+1
        back = ((n-p)//2)
    elif n%2 != 0 and p%2 != 0:
        front = (abs(1-p)//2)
        back = ((n-p)//2)
    pass

    if front > back:
        return(back)
    else:
        return(front)
    

if __name__ == '__main__':
    n = int(input())
    p = int(input())
    result = pageCount(n, p)
    print(str(result) + '\n')
