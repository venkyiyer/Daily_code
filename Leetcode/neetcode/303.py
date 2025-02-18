class NumArray:
    def __init__(self, nums):
        self.dummy =[]
        total = 0
        for n in nums:
            total+=n
            self.dummy.append(total)
    
    def sumRange(self, left, right):
        right = self.prefix[right] 
        left = self.prefix[left-1] if left>0 else 0
        
        return right - left

obj = NumArray([-2, 0, 3, -5, 2, -1])
print(obj.sumRange(0, 2))

