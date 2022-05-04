from math import pi
 
def ring_area(R, r):
    area = 'Error'
    if 0 <= r <= R:
        area = pi * (R ** 2- r ** 2)
    return area
 
print(ring_area(5, 3))
