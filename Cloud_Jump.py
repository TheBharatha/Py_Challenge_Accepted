def jumpingOnClouds(c):
    for i in range(c):
        print((i+3)%c)

if __name__ == '__main__':
    c = 6
    jumpingOnClouds(c)