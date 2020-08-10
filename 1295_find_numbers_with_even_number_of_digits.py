class Solution:
    def findNumbers(self, nums: list) -> int:
        answer = 0
        for num in nums:
            if len(str(num)) % 2 == 0:
                answer += 1

        return answer


s = Solution()
nums = [12, 345, 2, 6, 7896]
print(s.findNumbers(nums))
