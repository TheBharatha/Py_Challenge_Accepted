import os

def dayOfProgrammer(year):
    days, sams = 256, 0
    months = [31,28,31,30,31,30,31,31,30]
    
    if 1700 <= year <= 1917:
        months[8] = months[8] - 13
        if (year % 4) == 0:
            months[1] = months[1] + 1
    elif year == 1918:
        months[1] = months[1] - 13
    elif 1919 <= year <= 2700:
        if (year % 400) == 0 or (year % 4) == 0 and (year % 100) != 0:
            months[1] = months[1] + 1
    
    for month in months:
        if days > month:
            sams = sams + 1
            days = days - month
    
    if days > 0:
        sams += 1
    return(str(days).zfill(2) + '.' + str(sams).zfill(2) + '.' + str(year))

if __name__ == '__main__':
    year = int(input().strip())
    result = dayOfProgrammer(year)
    print(result + '\n')
