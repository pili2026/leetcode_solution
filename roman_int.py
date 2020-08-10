class Solution:
    def romanToInt(self, s):
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        res = roman[s[-1]]
        N = len(s)

        # range(start, stop[, step])
        for i in range(N - 2, -1, -1):
            if roman[s[i]] < roman[s[i + 1]]:
                res -= roman[s[i]]
            else:
                res += roman[s[i]]
        return res

a = Solution.romanToInt(Solution, 'CVIII')
print(a)
        