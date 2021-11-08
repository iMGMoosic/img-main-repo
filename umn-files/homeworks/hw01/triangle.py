# Lief Johnson
# joh19151
# CSCI 1133 Section 050
# Assignment 1

import math

b = float(input("Please enter the length of the shorter side (b): "))
A = float(input("Please enter the angle between sides b & c in degrees (A): "))
c = float(input("Please enter the length of the other side (c): "))

# law of cosines formula
a = math.sqrt(b ** 2 + c ** 2 - (2 * b * c * math.cos(math.radians(A))))

# law of sines formula
B = math.degrees(math.asin(b * math.sin(math.radians(A)) / a))

# since a triangle sums to 180º, 180º - the other 2 angles gets you the third
C = 180 - B - A

print("Side a is", a)
print("Side b is", b)
print("Side c is", c)
print("Angle A is", A)
print("Angle B is", B)
print("Angle C is", C)
