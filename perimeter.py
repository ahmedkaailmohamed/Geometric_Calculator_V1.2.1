import constants as cons

def perm_square(length):
  return round(4*(length), 3)

def perm_rectangle(length, width):
  return round(2*(length+width), 3)

def perm_circle(radius):
  return round(2*cons.pi()*radius, 3)