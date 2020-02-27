def countingValleys(n, s):
    count = steps = 0
    for units in s:
        if units == 'U':
            steps += 1
        else:
            steps -= 1
        
        if steps == 0 and units == 'U':
            count += 1
    return count


if __name__ == '__main__':
    n = int(input())
    s = input()
    result = countingValleys(n, s)
    print(str(result) + '\n')
