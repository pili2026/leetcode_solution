class Solution:
    def defangIPaddr(self, address: str) -> str:
        if address.find('.'):
            return address.replace('.', '[.]')


address = "1.1.1.1"
s = Solution()
print(s.defangIPaddr(address))
