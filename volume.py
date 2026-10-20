import constants as c
import math as m

def vol_cube(length):
  return round(m.pow(length, 3), 3)

def vol_cuboid(length, width, height):
  return round(length*width*height, 3)

def vol_sphere(radius):
  return round(c.pi()*m.pow(radius, 3), 3)

def vol_halfsphere(radius):
  return round((c.pi()*m.pow(radius, 3))/2, 3)

def vol_pyramid(length, height):
  return round((1/3)*(m.pow(length, 2))*height, 3)

def  vol_cone(radius, height):
  return round((1/3)*(c.pi()*m.pow(radius, 2))*height, 3)

def vol_cylinder(radius, height):
  return round(c.pi()*m.pow(radius, 2)*height, 3)