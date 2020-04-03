def saveThePrisoner(n, m, s):
    if m > n:
        print(m%n, abs(1-s))
        prisoner = (m%n) + abs(1-s)
    elif m < n:
        print('2')
        prisoner = (n%m) + s
    elif m == n:
        print('3')
        if s == 1:
            prisoner = m
        else:
            prisoner = s - 1
    return(prisoner)

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        nms = input().split()

        n = int(nms[0])

        m = int(nms[1])

        s = int(nms[2])

        result = saveThePrisoner(n, m, s)

        print(str(result) + '\n')