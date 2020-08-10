class Solution:
    def createTargetArray(self, nums: [int], index: [int]) -> [int]:
        target = []
        for n in range(len(nums)):
            target.insert(index[n], nums[n])
        
        return target


a = Solution()
nums = [0, 1, 2, 3, 4]
index = [0, 1, 2, 2, 1]
print(a.createTargetArray(nums, index))
