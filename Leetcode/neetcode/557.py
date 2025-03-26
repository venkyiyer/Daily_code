s = "Let's take LeetCode contest"

class Solution:
    def reverseWords(self, s):
        sp = s.split(' ')
        for ele in range(len(sp)):
            sp[ele] = sp[ele][::-1]
        
        return " ".join(sp)

obj = Solution()
print(obj.reverseWords(s))