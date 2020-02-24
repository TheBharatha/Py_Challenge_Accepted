#Maximum 69 Number
class Solution:
    def maximum69Number (self, num: int) -> int:
        mask = str(num)
        if '6' in mask:
            first = num + 3 * (10**(len(mask) - (mask.index('6') + 1)))
        else:
            first = num
        return(first)
