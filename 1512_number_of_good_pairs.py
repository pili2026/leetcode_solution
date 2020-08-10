class Solution:
    def numIdenticalPairs(self, nums: list) -> int:
        a = []
        for i in range(len(nums)):
            for j in range(len(nums), 0, -1):
                if nums[i] == nums[j-1] and i < j-1:
                    a.append((nums[i], nums[j-1]))
        return len(a)


# data = [1, 2, 3, 1, 1, 3]
data = [1, 2, 3]
s = Solution()
print(s.numIdenticalPairs(data))
