flowerbed = [1,0,0,0,0,1]
n = 2

class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        flowerbed = [0] + flowerbed + [0]
        for i in range(1, len(flowerbed)-1):
            if flowerbed[i] == 0:
                if (flowerbed[i-1] == 0) and (flowerbed[i+1]==0):
                    n-=1
                    flowerbed[i]=1
        
        if n>0:
            return False
        else:
            return True

obj = Solution()
print(obj.canPlaceFlowers(flowerbed, n))


# f = [0] + flowerbed + [0]
#         for i in range(1,len(f)-1):
#             if f[i-1] == 0 and f[i] == 0 and f[i+1] ==0:
#                 f[i] = 1
#                 n -=1
        
#         if n<=0:
#             return True
#         else:
#             return False