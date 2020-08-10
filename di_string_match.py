class Solution:
    def diStringMatch(self, S):
        N = len(S)
        
        # nI = 起始值(最小), nD = 字串總長度(最大值)
        nI, nD = 0, N
        res = []

        for s in S:
            if s == "I":
                res.append(nI)
                nI += 1
            else:
                res.append(nD)
                nD -= 1
        res.append(nI)
        return res

a = Solution()

print(a.diStringMatch("IIDIDIDD"))