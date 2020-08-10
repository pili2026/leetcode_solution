class Solution:
    # def longestCommonPrefix(self, strs):

    #     if not strs:
    #         return ""
    #     shortest_str = min(strs, key = len)
        
    #     for i, char in enumerate(shortest_str):
    #         for other in strs:
    #             if other[i] != char:
    #                 return shortest_str[:i]
    #     return shortest_str

    def longestCommonPrefix(self, strs):
        if not strs: return ""
        s1 = min(strs)
        s2 = max(strs)

        for i, c in enumerate(s1):
            if c != s2[i]:
                return s2[:i]
        return s1

a = Solution()
b = a.longestCommonPrefix(["dog","racecar","car"])
print(b)