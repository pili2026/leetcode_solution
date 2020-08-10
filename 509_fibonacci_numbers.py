
class Solution:
    def fib_recursive(self, n: int) -> int:
        import sys
        sys.setrecursionlimit(10000)

        if n == 0:
            return 0
        elif n == 1:
            return 1
        return self.fib_recursive(n - 1) + self.fib_recursive(n - 2)

    def fib(self, n: int) -> int:
        f = {0: 0, 1: 1}
        for i in range(2, n + 1):
            f[i] = f[i - 1] + f[i - 2]
        return f[n]


a = Solution()
print(a.fib(2))
