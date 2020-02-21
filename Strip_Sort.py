def sortInfo(name):
    names = sorted(name)
    for i in range(len(names)):
        print(names[i])

if __name__ == '__main__':
    N = int(input())
    nameList = list()
    for N_itr in range(N):
        firstNameEmailID = input().split()
        firstName = firstNameEmailID[0]
        emailID = firstNameEmailID[1]
        email = str(emailID)
        if '@gmail.com' in email:
            nameList.append(firstName)
    sortInfo(nameList)
