class Solution:
    def clearDigits(self, s):
        result = []
        delete_count = 0
        
        for i in reversed(range(len(s))):
            if s[i].isdigit():
                delete_count += 1
            else:
                if delete_count > 0:
                    delete_count -= 1
                else:
                    result.append(s[i]  )

obj = Solution()
print(obj.clearDigits("cb34"))