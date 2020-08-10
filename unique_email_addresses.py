class Solution:
    def uniqueEmailAddresses(self, emails):
        res = set()

        for email in emails:
            name, domain = email.split("@")
            name = name.split('+')[1].replace(".", "")
            res.add(name + "@" + domain)
        return len(res)

a = Solution()
print(a.uniqueEmailAddresses(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]))