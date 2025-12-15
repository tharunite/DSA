1class Solution:
2    def defangIPaddr(self, address: str) -> str:
3        return address.replace('.','[.]')
4        