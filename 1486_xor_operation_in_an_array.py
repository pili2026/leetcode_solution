# nums[i] = start + 2*i
class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        output = 0

        for num in range(start, start + (2 * n), 2):
            output ^= num

        return output


n = 4
start = 3
s = Solution()
print(s.xorOperation(n, start))
