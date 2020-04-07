def jumpingOnClouds(c):
    start = jumps = 0
    traverse = len(c) - 1
    while start <= traverse:
        try:
            if c[start + 2] == 0:
                jumps += 1
                start += 2
                print(jumps, start)
            else:
                jumps += 1
                start += 1
                print(jumps, start)
        except:
                jumps += 1
                start += 1
                print(jumps, start)
    return(jumps)

if __name__ == '__main__':

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    print(str(result) + '\n')