def further(kp_string,i,n):
    one_pair = kp_string.split(" ")
    phoneBook[one_pair[0]] = one_pair[1]
    more = True
    if i == n:
        while more == True:
            try:
                check = str(input())
                if len(check) > 0:
                    if check in phoneBook:
                        print('%s=%s' % (check,str(phoneBook[check])))
                    else:
                        print('Not found')
                else:
                    more = False
            except:
                more = False
    else:
        pass

if __name__ == '__main__':
    phoneBook={}
    n = int(input())
    for i in range(n):
        first_Check = str(input())
        if len(first_Check) > 0:
            further(first_Check,(i+1),n)
