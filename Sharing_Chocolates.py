def birthday(s, d, m):
    can = 0
    if len(s) > 1:
        for sq in range(len(s)-(m-1)):
            if sum(s[sq:sq+m]) == d:
                can += 1
    else:
        if s[0] == d:
            can = 1
    return(can)

if __name__ == '__main__':
    n = int(input().strip())
    s = list(map(int, input().rstrip().split()))
    dm = input().rstrip().split()
    d = int(dm[0])
    m = int(dm[1])
    result = birthday(s, d, m)
    print(str(result) + '\n')
