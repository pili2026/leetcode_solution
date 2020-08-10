class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        i = 0
        for j in J:
            s_sum = S.count(j)
            i += s_sum
        return i


j = "z"
s = "ZZ"
a = Solution()
print(a.numJewelsInStones(j, s))