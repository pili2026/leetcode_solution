class Solution:
    # def smallerNumbersThanCurrent(self, nums: list) -> list:
    #     answers = []
    #
    #     for i in range(len(nums)):
    #         answer = 0
    #         for j in range(len(nums), 0, -1):
    #             if j-1 != i and nums[j-1] < nums[i]:
    #                 answer += 1
    #         answers.append(answer)
    #
    #     return answers

    def smallerNumbersThanCurrent(self, nums: list) -> list:
        answers = []
        sort_nums = sorted(nums)

        for index in range(len(sort_nums)):
            answers.append(sort_nums.index(nums[index]))
        return answers


nums = [6, 5, 4, 8]
s = Solution()
print(s.smallerNumbersThanCurrent(nums))