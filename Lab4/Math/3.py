import math
n = float(input())
s = float(input())

area_polygon = (n * s**2) / (4 * math.tan(math.pi / n))
print (area_polygon)