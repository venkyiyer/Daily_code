class Solution:
    def uniqueOccurences(self, arr):
        hm = {}
        for i in arr:
            if i in hm:
                hm[i] += 1
            else: 
                hm[i] = 1
        
        lst_occur = list(hm.values())
        count_hm = {}
        for j in lst_occur:
            if j in count_hm:
                return False
            else:
                count_hm[i] =1
        
        return True 

obj = Solution()
obj.uniqueOccurences([1,2,2,1,1,3])
