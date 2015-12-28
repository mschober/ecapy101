# Review
# - lists
# - for-each

# Topics
# - to string
# - polymorphism

# Key Terms
# - class
# - attribute
# - method



class Rect():
    name = "Rectangle"

    def __str__(self):
        return self.name


class Circ():
    name = "Circle"

    def __str__(self):
        return self.name


class Tri():
    name = "Triangle"

    def __str__(self):
        return self.name


shapes = [
  Rect()
, Circ()
, Tri()
]

for shape in shapes:
    print shape

tri = Tri()
tri.name += " Overriden"

print tri
