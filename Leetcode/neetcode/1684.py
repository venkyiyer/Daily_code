class Solution:
    def countConsistentStrings(self, allowed, words):
        count = 0 
        for w in words:
            if set(w).issubset(set(allowed)):
                count +=1

        return count

obj = Solution()
print(obj.countConsistentStrings(allowed = "cad", words = ["cc","acd","b","ba","bac","bad","ac","d"]))
