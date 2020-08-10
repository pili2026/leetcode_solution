class Solution:
    def numberOfSteps (self, num: int):
        counter = 0

        while num > 0:
            if num % 2 == 0:
                num = num // 2
            else:
                num -= 1
            counter += 1
        return counter


a = Solution()
b = a.numberOfSteps(20)
print(b)
