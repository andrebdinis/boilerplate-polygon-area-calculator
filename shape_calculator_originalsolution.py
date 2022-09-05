class Rectangle:
  w = 0
  h = 0

  def __init__(self, width, height):
    self.w = width
    self.h = height
    #print("Rectangle constructed")

  def __str__(self):
    return "Rectangle(width=%d, height=%d)" % (self.w, self.h)

  def set_width(self, width):
    self.w = width

  def set_height(self, height):
    self.h = height

  def get_area(self):
    return self.w * self.h

  def get_perimeter(self):
    return (2 * self.w) + (2 * self.h)

  def get_diagonal(self):
    return ( ((self.w ** 2) + (self.h ** 2)) ** 0.5 )

  def get_picture(self):
    if self.w > 50 or self.h > 50: return "Too big for picture."
    pic = ""
    for i in range(self.h):
      pic += "".ljust(self.w, "*") + "\n"
      #if i+1 < self.h: pic += "\n"
    return pic

  def get_amount_inside(self, shape):
    return int( (self.w / shape.w) * (self.h / shape.h) )


# Square inherits from Rectangle
class Square (Rectangle):
  
  def __init__(self, side):
    self.w = side
    self.h = side
    #print("Square constructed")

  def __str__(self):
    return "Square(side=%d)" % (self.w)

  def set_side(self, side):
    self.w = side
    self.h = side

  def set_width(self, side):
    self.set_side(side)
    
  def set_height(self, side):
    self.set_side(side)