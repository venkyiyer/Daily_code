class Solution:
    def finalValueAfterOperations(self, operations: List[str]):
        x = 0
        for sign in operations:
            if sign == 'X++' or sign == '++X':
                x +=1
            else:
                x -=1
        
        return x

obj  = Solution()
obj.finalValueAfterOperations(['X++', '--X'])