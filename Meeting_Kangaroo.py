import math

def kangaroo(k1, v1, k2, v2):
    pos_k1, pos_k2 = k1, k2

    if k1 < k2 and v1 < v2:
        return('NO')
    elif k1 < k2 and v1 > v2:
        for i in range(10000):
            if pos_k1 < math.inf:
                pos_k1 = pos_k1 + v1
            if pos_k2 < math.inf:
                pos_k2 = pos_k2 + v2
            if pos_k1 == pos_k2:
                return('YES')
        return('NO')
    elif k1 == k2 and v1 == v2:
        return('YES')
    elif k1 > k2 and v1 == v2:
        return('NO')
    elif k1 == k2 and v1 < v2:
        return('NO')
    elif k1 == k2 and v1 > v2:
        return('NO')
    elif k1 < k2 and v1 == v2:
        return('NO')

if __name__ == '__main__':
    x1V1X2V2 = input().split()
    x1 = int(x1V1X2V2[0])
    v1 = int(x1V1X2V2[1])
    x2 = int(x1V1X2V2[2])
    v2 = int(x1V1X2V2[3])
    result = kangaroo(x1, v1, x2, v2)
