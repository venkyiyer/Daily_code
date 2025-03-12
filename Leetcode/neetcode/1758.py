s = "1111"

class Solution:
    def minOperations(self, s):
        count = 0
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                print(s[i])
                print(s[i+1])
                if s[i] == '0':
                    s[i+1] = '1'
                else:
                    s[i+1] = '0'
                count +=1
            else:
                continue

obj = Solution()
print(obj.minOperations(s))



# if i % 2:
#                 count += 1 if s[i] == '0' else 0
#             else:
#                 count +=1 if s[i] == '1' else 0
        
#         return min(count, len(s) - count)