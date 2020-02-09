def finer(act,exp):
    y_dif = act[2] - exp[2]
    m_dif = act[1] - exp[1]
    d_dif = act[0] - exp[0]
    if y_dif >= 1:
        fine = 10000
        return fine
    elif m_dif >= 1 and y_dif == 0:
        fine = 500 * m_dif
        return fine
    elif d_dif >= 1 and m_dif == 0 and y_dif == 0:
        fine = 15 * d_dif
        return fine
    elif d_dif <= 0 and m_dif <= 0 and y_dif <= 0:
        fine = 0
        return fine
    elif d_dif <= 0 and m_dif <= 0 and y_dif >= 1:
        fine = 10000
        return fine
    elif d_dif <= 0 and m_dif >= 1 and y_dif <= 0:
        fine = 0
        return fine
    elif d_dif >= 0 and m_dif >= 1 and y_dif == 0:
        fine = m_dif * 500
        return fine
    elif d_dif < 0 and m_dif >= 1 and y_dif == 0:
        fine = m_dif * 500
        return fine
    elif d_dif >= 1 and m_dif >= 0 and y_dif >= 1:
        fine = 10000
        return fine
    else:
        fine = 0
        return fine
    
if __name__ == '__main__':
    act = input()
    act = list(map(int, act.rstrip().split()))
    exp = input()
    exp = list(map(int, exp.rstrip().split()))
    pay = finer(act,exp)
    print(pay)
