#Python, physics test score and names of a class size N
def second(test):
    nest = (sorted(test, key = lambda a:a[1]))
    names, sec_low,i,low = '', None, 0, nest[0]
    found = True
    while found:
        if nest[i][1] > low[1]:
            sec_low = nest[i]
            found = False
        i += 1
    names = sorted([nest[i][0] for i in range(len(nest)) if nest[i][1] == sec_low[1]])
    for name in names:
        print(name)

#Driving code
if __name__ == '__main__':
    test = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        test.append([name, score])
    second(test)
