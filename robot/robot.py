

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
