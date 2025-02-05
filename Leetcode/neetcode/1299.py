arr = [17,18,5,4,6,1]

class Solution:
    def replaceElement(self, arr):
        len_arr = len(arr)
        if len_arr>1:
            for i in range(len_arr-1):
                get_max = max(arr[i+1:])
                arr[i] = get_max
            arr[-1] = -1
            return arr
        else:
            arr = [-1]
            return arr

obj = Solution()
print(obj.replaceElement(arr))