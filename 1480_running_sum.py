class Solution:
    def runningSum(self, nums: list) -> list:
        answer = 0
        answer_list = []
        for num in nums:
            answer += num
            answer_list.append(answer)
        return answer_list


data = [1,2,3,4]
a = Solution()
print(a.runningSum(data))
