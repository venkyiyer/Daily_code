emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]

class Solution:
    def numUniqueEmails(self, emails):
        demo = set()
        for e in emails:
            local, domain = e.split('@')
            local = local.split('+')[0]
            local = local.replace(".", "")
            demo.add((local, domain))
        
        return len(demo)

obj = Solution()
print(obj.numUniqueEmails(emails))