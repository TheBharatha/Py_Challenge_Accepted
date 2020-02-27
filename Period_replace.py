class Solution:
    def defangIPaddr(self, address: str) -> str:
        defange = ''
        for ip in address:
            if ip.isnumeric():
                defange = defange + ip
            else:
                defange = defange + '[.]'
        return defange
