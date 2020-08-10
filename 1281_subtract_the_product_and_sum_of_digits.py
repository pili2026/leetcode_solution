class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        d_sum = 0
        d_pro = 1
        n_str = str(n)

        for i in n_str:
            d_sum += int(i)
            d_pro *= int(i)

        answer = d_pro - d_sum

        return answer


s = Solution()
n = 234
print(s.subtractProductAndSum(n))
