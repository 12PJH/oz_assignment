import math

def triangle_area(base, height):
    return (base * height) / 2

def circle_area(radius):
    return math.pi * radius ** 2

def rectangular_prism_volume(length, width, height):
    return length * width * height

def rectangular_prism_surface_area(length, width, height):
    return 2 * (length * width + length * height + width * height)
