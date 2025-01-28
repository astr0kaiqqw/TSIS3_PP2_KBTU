import math

def sphere_volume(radius):
    return (4/3) * math.pi * radius**3


radius = float(input("Enter the radius of the sphere: "))
volume = sphere_volume(radius)
print(f"The volume of the sphere is: {volume}")
