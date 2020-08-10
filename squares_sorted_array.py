class Solution:
    def sortedSquares(self, A):
        L = list()
        for i in A:
            L.append(i ** 2)
        L.sort()
        return L

a = Solution()
print(a.sortedSquares([1,4,8,9,-7,5,-2,2]))