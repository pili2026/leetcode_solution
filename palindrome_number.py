class Solution(object):
    def isPalindrome(self, x):

        s = str(x)
        i = 0

        if len(s) > 1:
            # len(s) / 2) + 1, 將字串長度切成一半，從另一半的第一個字開始
            while i < (len(s) / 2) + 1:
                # len(s) - 1 - i, 從字串最大值開始向前算
                if s[i] == s[len(s) - 1 - i]:
                    i = i+ 1
                else:
                    return False
            return True
        return True

a = Solution.isPalindrome(Solution, 121121)
print(a)