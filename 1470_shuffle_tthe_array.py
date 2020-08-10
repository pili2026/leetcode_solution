class Solution:
    def shuffle(self, nums: list, n: int) -> list:

        result = []
        for i in range(n):
            result.extend([nums[i]]+[nums[i+n]])
        return result


data = [2,5,1,3,4,7]
n = 3

s = Solution()
print(s.shuffle(data, n))
