class Solution(object):
    def twoSum(self, nums: list, target: int) -> list:
        seen = {}
        for i, v in enumerate(nums):
            remaining = target - v
            if remaining in seen:
                return [seen[remaining], i]
            seen[v] = i
        return []


s = Solution()
data = [9, 10, 11, 15]
result = 21
s.twoSum(data, result)
