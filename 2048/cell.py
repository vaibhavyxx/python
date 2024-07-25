#cells of 2048 game
#cannot have multiple constructors
#properties don't exist you make functions instead 
#private does not exist in python so it's fine

class cell:
    def __init__(self,x,y):
        self.value = 0
        self.x = x
        self.y = y
        self.isFull = False

