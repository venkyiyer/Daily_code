class Solution:
    def largestAltitude(self,gain):
        lst = [0]
        for i in range(len(gain)):
            temp = lst[i] + gain[i]
            lst.append(temp)
        
        return max(lst)

obj = Solution()
obj.largestAltitude([-5,1,5,0,-7])