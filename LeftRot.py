# Complete the rotLeft function below.
def rotLeft(a, d):
    partOne = a[:d]
    a = a[d:]
    a.extend(partOne)
    print(a)

if __name__ == '__main__':
    nd = input().split()
    n = int(nd[0])
    d = int(nd[1])
    a = list(map(int, input().rstrip().split()))
    result = rotLeft(a, d)
    print(' '.join(map(str, result)))