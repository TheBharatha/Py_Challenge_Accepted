class Solution:
    def bitwiseComplement(self, N: int) -> int:
        binaryValue = str(bin(N))
        binaryValue = binaryValue[2:]
        binaryValue = binaryValue.replace('0', '%temp%').replace('1', '0').replace('%temp%', '1')
        binaryValue = int(binaryValue,2)
        return(binaryValue)
