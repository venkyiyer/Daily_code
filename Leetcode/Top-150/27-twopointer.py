nums = [2]
val  = 3
l, r = 0,1

for r in range(1,len(nums)):
    if nums[l]!= val:
        l+=1
    else:
        if nums[l]==val and nums[r]!= val:
            nums[l], nums[r] = nums[r], nums[l]
            l +=1

print(l)
print(nums)

k = 0

for i in range(len(nums)):
    if nums[i]!=val:
        nums[k] = nums[i]
        k+=1
print('k is:', k)


        
