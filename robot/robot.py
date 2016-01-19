

class Head():
    pass

class Torso():
    pass

class LeftArm():

    def shoot(self):
        print "robot shoots weapon in left arm"

class RightArm():

    def shoot(self):
        print "robot shoots weapon in right arm"

class Legs():

    def walk(self):
        print "robot walks forward"


class Robot():

    def __init__(self):
        self.head = Head()
        self.torso = Torso()
        self.left_arm = LeftArm()
        self.right_arm = RightArm()
        self.legs = Legs()
        #What about self.treads, self.wheels

    def move(self):
        self.legs.walk()

    def fire_right(self):
        self.right_arm.shoot()

    def fire_left(self):
        self.left_arm.shoot()


class GridMap():

    def __init__(self):
        self.grid = [[],[]]


    def place(self,robot):
        self.grid[0].append(robot)

class Quest():

    def __init__(self):
        self.grid = GridMap()


    def print_situation(self):
        print """
        You are standing at {0} in the map. You can go right.
        """.format("start position")

    def start_game(self):
        self.robot = Robot()
        self.grid.place(self.robot)
        self.print_situation()



