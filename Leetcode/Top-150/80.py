nums = [0,0,1,1,1,1,2,3,3]

index = 1
occ = 1

for i in range(1, len(nums)):
    if nums[i] == nums[i-1]:
        occ +=1
    else:
        occ = 1

    if occ <=2:
        nums[index] = nums[i]
        index +=1

print(index)
print(nums)