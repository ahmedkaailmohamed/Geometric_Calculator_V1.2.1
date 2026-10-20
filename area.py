import constants as cons
import math as m

def area_square(length):
  return round(length*length, 3)

def area_rectangle(length, width):
  return round(length*width, 3)

def area_circle(radius):
  return round(cons.pi()*(radius*radius),3)

def area_triangle1(base, height):
  return round((1/2)*base*height, 3)

def area_triangle2(len_a, len_b, ang_C):
  return round((1/2)*len_a*len_b*m.sin(m.radians(ang_C)),3)

def area_parallelogram(length, height):
  return round(length*height, 3)

def area_trapezium(len_a, len_b, height):
  return round((1/2)*(len_a+len_b)*height, 3)