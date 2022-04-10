class Solution():

    def firstUniqChar(self, s):
        dic = {}
        for i in s:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        for j in range(len(s)):
            if dic[s[j]] == 1:
                return j
        return -1
    
obj = Solution()
print(obj.firstUniqChar("aabb"))
            