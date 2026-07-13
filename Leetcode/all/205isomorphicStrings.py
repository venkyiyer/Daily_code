class Solution:
    def isIsomorphic(self,s:str,t:str):
        mapST, mapTS = {}, {}
        for c1, c2 in zip(s,t):
            if ((c1 in mapST and mapST[c1]!= c2) or (c2 in mapTS and mapTS[c2]!=c1)):
                return False

            mapST[c1] = c2
            mapTS[c2]=c1
        
        return True
    
obj = Solution()
obj.isIsomorphic(s='egg', t='add')