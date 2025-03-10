s = "mgntdygtxrvxjnwksqhxuxtrv"

class Solution:
    def maxLengthBetweenEqualCharacters(self, s):
        maxlength = []
        for i in range(0, len(s)-1):
            if len(s) == 2 and s[i] == s[i+1]:
                return 0
            else:
                for j in range(i+1, len(s)):
                    if s[i] == s[j]:
                        maxlength.append((j-1) - i)
        if maxlength:
            return max(maxlength)
        else:
            return -1


obj = Solution()
print(obj.maxLengthBetweenEqualCharacters(s))
            