class Solution:
    def balancedStringSplit(self, s: str) -> int:
        result = 0
        count = 0

        for s_str in s:
            if s_str == "R":
                count += 1
            else:
                count -= 1

            if count == 0:
                result += 1
        return result


a = Solution()
s = "RLRRLLRLRL"
print(a.balancedStringSplit(s))
