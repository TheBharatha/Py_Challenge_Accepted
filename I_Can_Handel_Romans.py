def roam(s):
    guide = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D': 500, 'M':1000}
    value = prev_char = 0
    for char in s[::-1]:
        if guide[char] >= prev_char:
            prev_char = guide[char]
            value = value + guide[char]
        else:
            value = value - guide[char]
        print(value)
    print(value)
    
roam('MMMDCCCLXXIV')   
