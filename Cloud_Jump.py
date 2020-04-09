from decimal import Decimal
def jumpingOnClouds(c, k):
    stop = False
    energy = 100
    index = 0
    while stop == False:
        for _ in range(k):
            energy -= 1
            index = (index + k)%len(c)
            if c[index] == 1:
                energy -= 2
            print('Index: ',index, 'Energy: ', energy)
            if index == 0:
                stop = True
                break
    print(energy)

if __name__ == '__main__':
    c = [0,0,1,0,0,1,1,0]
    k = 2
    jumpingOnClouds(c, k)