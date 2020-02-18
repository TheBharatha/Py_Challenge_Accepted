def roam(s):
    Guide = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D': 500, 'M':1000}
    num = prev_char = 0
    for char in s[::-1]:
        if Guide[char] >= prev_char:
            prev_char = Guide[char]
            num = num + Guide[char]
        else:
            num = num - Guide[char]
    print(num)
    
roam('MCMXCIV')   
