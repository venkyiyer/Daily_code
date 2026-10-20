class Solution:
    def guess(self, num, pick):
        if num > pick:
            return -1
        elif num< pick:
            return 1
        else:
            return 0

    def guessNumber(self, n, pick):
        l, r = 0, n
        while l < r: 
            m = (l + r) // 2
            if pick > m:
                l = m + 1
            if pick < m:
                r = m - 1
            else: 
                return n[m]
            
            
