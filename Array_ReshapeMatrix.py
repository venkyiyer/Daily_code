class Solution(object):
    def matrixReshape(self, nums, r, c):
        if len(nums) * len(nums[0]) != r * c:
            return nums
        
        ans = [[]]
        for i in range(len(nums)):
            for j in range(len(nums[0])):
                k = nums[i][j]
                if len(ans[-1]) < c:
                    ans[-1].append(k)
                else:
                    ans.append([k])
        return ans

obj = Solution()
print(obj.matrixReshape([[1,2],[3,4]], r = 2, c = 4))