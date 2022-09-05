from rectangle import Rectangle


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