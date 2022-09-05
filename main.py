# This entrypoint file to be used in development. Start by reading README.md
import shape_calculator
from shape_calculator import Rectangle, Square
from unittest import main


# Rectangle example
rect = Rectangle(5, 10)
print(rect.get_area())
rect.set_width(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

# Square example
sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())


# Run unit tests automatically
main(module='test_module', exit=False)