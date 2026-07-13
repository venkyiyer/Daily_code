from collections import deque
class RecentCounter:
    def __init__(self):
        self.queue = []
    
    def ping(self,t):
        self.queue.append(t)
        while self.queue[0]< t - 3000:
            self.queue.pop(0)

        print(len(self.queue))

obj = RecentCounter()
obj.ping(1)
obj.ping(100)
obj.ping(3001)
obj.ping(3002)