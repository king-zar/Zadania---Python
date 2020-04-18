# program counts area and volume of the cuboid
# 3 lines below - loading edges
a = float(input("Write length of the first edge of base: "))
b = float(input("Write length of the second edge of base: "))
H = float(input("Write height of the cuboid: "))

# 3 lines below - counting areas
basesArea = 2*a*b
wallsArea = 2*(a+b)*H
cuboidArea = basesArea + wallsArea

print("Area of cuboid: ", cuboidArea) # writing result for area

cuboidVolume = a*b*H # counting volume
print("Volume of cuboid: ", cuboidVolume) # writing result for volume