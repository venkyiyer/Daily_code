class MyhashMap:
    
    def __init__(self):
        self.hs = {}

    def add(self, key):
        self.hs.add(key)
    
    def remove(self, key):
        if key in self.hs:
            self.hs.remove(key)

    def contains(self, key):
        if key in self.hs:
            return True
        else:
            return False

