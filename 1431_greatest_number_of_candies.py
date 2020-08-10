class Solution:
    def kidsWithCandies(self, candies: list, extraCandies: int) -> list:
        max_candy = max(candies)
        result = []

        for candy in candies:
            if candy + extraCandies >= max_candy:
                result.append(True)
            else:
                result.append(False)
        return result


candies = [4, 2, 1, 1, 2]
extraCandies = 1
s = Solution()
print(s.kidsWithCandies(candies, extraCandies))
