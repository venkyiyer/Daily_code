class Solution:
    def reverseWords(self, s):
        x = s.split(' ')[::-1]
        # new_list = [ele for ele in x if ele.strip()]
        stri = ' '.join([ele for ele in x if ele.strip()])
        print(stri)

obj = Solution()
obj.reverseWords("  This is    Blue")