class Solution:
    def decompressRLElist(self, nums: list) -> list:
        answers = []

        for i in range(0, len(nums), 2):
            [freq, val] = [nums[i], nums[i + 1]]
            answers.extend([val] * freq)

        return answers


s = Solution()
nums = [1,2,3,4]
print(s.decompressRLElist(nums))
