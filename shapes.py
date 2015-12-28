# Review
# - lists
# - for-each

# Topics
# - to string
# - polymorphism
# - refactor
# - inheritance
# - help command
# - dir command


# Key Terms
# - class
# - attribute
# - method
# - refactor
# - inheritance
# - docstring
# - instance
# - object


class Shape():
    """Abstract shape object with to string defined"""

    def __str__(self):
        return self._name

class Rect(Shape):
    """A Rectangle implementation of Shape"""
    _name = "Rectangle"


class Circ(Shape):
    """A Circle implementation of Shape"""
    _name = "Circle"


class Tri(Shape):
    """A Triangle implementation of Shape"""
    _name = "Triangle"

shapes = [
  Rect()
, Circ()
, Tri()
]

for shape in shapes:
    print shape
