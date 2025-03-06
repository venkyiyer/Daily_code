s = "1111"

class Solution:
    def minOperations(self, s):
        count = 0
        for i in range(len(s)-1):
            if s[i] == '0':
                if s[i+1] == '1':
                    continue
                else:
                    count+=1
            else:
                if s[i+1] == '0':
                    continue
                else:
                    count +=1
        
        return count
    
obj = Solution()
print(obj.minOperations(s))
