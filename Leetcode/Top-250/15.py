class Solution:
    def threesum(self, nums):
        nums.sort()
        a, l, r = 0,0, len(nums)-1
        arr = []
        while l < r:
            if nums[a] + nums[l] + nums[r] > 0:
                r-=1
            elif nums[a] + nums[l] + nums[r] < 0:
                l +=1
            else: 
                arr.append([a,l,r])
            a+=1
        
        return arr

obj = Solution()
print(obj.threesum([-1,0,1,2,-1,-4]))