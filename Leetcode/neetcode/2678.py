class Solution:
    def countSeniors(self, details):
        count = 0
        for d in details:
            print(d[11:13])
            if int(d[11:13]) > 60:
                count +=1
        
        return count

obj = Solution()
print(obj.countSeniors(["7868190130M7522","5303914400F9211","9273338290F4010"]))