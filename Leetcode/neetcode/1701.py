class Solution:
    def averageWaitingTime(self, customers):
        cooking_time = customers[0][0] + customers[0][1]
        avg_time = cooking_time - customers[0][0]
        for i in range(1, len(customers)):
            if cooking_time > customers[i][0]:
                avg_time += (cooking_time + customers[i][1]) - customers[i][0]
                cooking_time += customers[i][1]
            else:
                avg_time += (customers[i][0] + customers[i][1]) - customers[i][0]
                cooking_time = customers[i][0] + customers[i][1]
        
        avg = avg_time / len(customers)
        return avg
    
obj = Solution()
print(obj.averageWaitingTime(customers = [[2,3],[6,3],[7,5],[11,3],[15,2],[18,1]]))