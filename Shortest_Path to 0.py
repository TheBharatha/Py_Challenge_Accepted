n, count = 999, 0
if 0 <= n <= 10**6:
    while not n == 0:
        if n%2 == 1:
            n = n-1
            count += 1
        elif n%2 == 0:
            n = n/2
            count += 1
print(count)
