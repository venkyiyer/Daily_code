from collections import defaultdict
class Solution:
    def relativeSortArray(self, arr1, arr2):
        end = []
        count_dict = defaultdict(int)

        for i in arr1:
            if i not in arr2:
                end.append(i)
            count_dict[i] +=1
        end.sort()
    
        res = []
        for n in arr2:
            for _ in range(count_dict[n]):
                res.append(n)
        
        return res + end
            

obj = Solution()
print(obj.relativeSortArray(arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]))