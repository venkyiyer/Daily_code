class solution():

    def twoSum(self,listofNumbers, target):
        buffer_dictionary = {}
        for i in range(len(listofNumbers)):
            if listofNumbers[i] in buffer_dictionary:
                return [buffer_dictionary[listofNumbers[i]], i] 
            else:
                buffer_dictionary[target - listofNumbers[i]] = i 
obj = solution()
print(obj.twoSum([3,2,3], 6))