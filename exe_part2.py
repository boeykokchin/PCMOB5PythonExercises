### Exercise 4 ###
print('### Exercise 4 - Working with lists ###')
numbers_list = [12, 10, 32, 3, 66, 17, 42, 99, 20]
for number in numbers_list:
    print(number, number**2)
print('\n')
### Exercise 4 ###

### Exercise 5 ###
print('### Exercise 5 - Dice ###')
import random
def roll5dice():
   for i in range(5):
       dice_num = i + 1
       roll = random.randint(1, 7)
       print("Dice", dice_num, "rolls", roll)
roll5dice()
print('\n')
### Exercise 5 ###

### Exercise 6 ###
print('### Exercise 6 - Class ###')
class Point:
    """ Point class for working with x,y coordinates. """

    def __init__(self, initX, initY):
        """ Create a new point at the given coordinates. """
        self.x = initX
        self.y = initY

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distanceFromOrigin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

p = Point(5, 5)
print(p.distanceFromOrigin())
p2 = Point(10, 10)
print(p2.distanceFromOrigin())
### Exercise 6 ###
