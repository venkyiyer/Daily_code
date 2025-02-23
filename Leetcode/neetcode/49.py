strs = ["eat","tea","tan","ate","nat","bat"]
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
        res = defaultdict(list)

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord('a')] +=1
            
            res[tuple(count)].append(s)
        print(res.values())
        return res.values(0)
    
obj = Solution()
print(obj.groupAnagrams(strs))