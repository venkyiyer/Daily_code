from collections import defaultdict
class Solution:
    def makeEqual(self, words):
        cnt_dict = defaultdict(int)
        for w in words:
            for i in w:
                cnt_dict[i] +=1
        
        for j in cnt_dict:
            if cnt_dict[j] % len(words):
                return False
        
        return True

obj = Solution()
print(obj.makeEqual(["abc","aabc","bc"]))