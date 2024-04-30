class Base:

    def __init__(self, length):
        self.length = length
        print('Base__init__')

class square(Base):
    super.__init__()
    print('square__init__')

c1 = square()

