class Solution:
    def removeDulicates(self, nums):
        if len(nums) == 0:
            return 0
        j = 0

        for i in range(0, len(nums)):
            if nums[i] != nums[j]:
                nums[j + 1] = nums[i]
                j += 1
        return j + 1
a = Solution.removeDulicates(Solution, [1,1,1,4,5])
print(a)