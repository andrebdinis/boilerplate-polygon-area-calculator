import sys
sys.path.insert(0, './shapes/')
#print(sys.path)
from rectangle import Rectangle
from square import Square

# SPECIAL NOTE:
# As a test and to learn how to use/import manual-made packages: decided to create a "shapes" package (a folder which contains __init__.py file) so I could import both classes (Rectangle and Square) from modules "rectangle.py" and "square.py".
# For that to work: imported sys library, inserted a new path ("./shapes/") on its list of paths (sys.path) to aknowledge its existence, and from there imported the classes Rectangle and Square from the modules rectangle.py and square.py, respectively.

# SOURCE: https://stackoverflow.com/a/50474562/19788371
# DOC: https://docs.python.org/3/reference/import.html#package-relative-imports