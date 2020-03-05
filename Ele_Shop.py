def getMoneySpent(keyboards, drives, b):
    cart = list()
    cart.append([i+j for i in keyboards for j in drives if i+j <= b])
    try:
        return(max(cart[0]))
    except:
        return(-1)

if __name__ == '__main__':
    bnm = input().split()
    b = int(bnm[0])
    n = int(bnm[1])
    m = int(bnm[2])
    keyboards = list(map(int, input().rstrip().split()))
    drives = list(map(int, input().rstrip().split()))

    moneySpent = getMoneySpent(keyboards, drives, b)
    
    print(str(moneySpent) + '\n')
