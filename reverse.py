class Solution:
    def reverse(self, x):
        is_neg = False
        if x < 0:
            x = x * -1
            is_neg = True

        string = str(x)
        result = (-1 * int(string[::-1])) if is_neg else int(string[::-1])
        return result if (-2 ** 31 <= result <= 2 ** 31) else 0


a = Solution()
print(a.reverse(-1123))
