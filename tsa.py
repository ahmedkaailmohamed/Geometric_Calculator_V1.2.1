import constants as c


def tsa_cube(length):
    return round(6 * (length * length), 3)


def tsa_cuboid(length, width, height):
    return round(2 * ((length * width) + (width * height) + (length * height)), 3)


def tsa_sphere(radius):
    return round(4 * (c.pi() * (radius * radius)), 3)


def csa_halfsphere(radius):
    return round(2 * (c.pi() * (radius * radius)), 3)


def tsa_halfsphere(radius):
    return round(3 * (c.pi() * (radius * radius)), 3)


def csa_cylinder(radius, height):
    return round(2 * c.pi() * radius * height, 3)


def tsa_cylinder(radius, height):
    return round((2 * c.pi() * radius * height) + 2 * (c.pi() * (radius * radius)), 3)


def csa_cone(radius, s_height):
    return round(c.pi() * radius * s_height, 3)


def tsa_cone(radius, s_height):
    return round((c.pi() * radius * s_height) + (c.pi() * (radius * radius)), 3)
