class Solution:

    def sortdict(self, dict):
        return sorted(dict.items(), key=lambda x:x[0])
    
    def sortdict_1(self, dict):
        return sorted(dict, key=dict.get, reverse=False )



obj = Solution()
print(obj.sortdict({'a':40, 'b': 20, 'c':30, 'd':10})) 