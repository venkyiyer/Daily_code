class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.big = big
        self.medium = medium
        self.small = small

    def addCar(self, carType: int) -> bool:
        if carType == 1:
            if self.big == 0:
                return False 
            else: 
                self.big -=1
                return True
        elif carType == 2:
            if self.medium == 0:
                return False
            else:
                self.medium -=1
                return True
        else:
            if self.small == 0:
                return False
            else:
                self.small -=1
                return True