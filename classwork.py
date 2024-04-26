
import math

def calculate_circle_area(radius):
 return math.pi * (radius ** 2)

radius = float (input ("enter the radius of the circle:"))
area = calculate_circle_area(radius)

print("The area of the circle is: ", area)
def cone_surface_area(radius, height):
    return math.pi * radius * (radius + math.sqrt(height**2 + radius**2))

radius = radius
height = float (input ("enter the height of the circle:"))
print("Surface area of the cone:", cone_surface_area(radius, height))

def cylinder_surface_area(radius, height):
    return 2 * math.pi * radius * (radius + height)

print("Surface area of the cylinder:", cylinder_surface_area(radius, height))

def sector_area(radius, angle):
    return 0.5 * radius**2 * angle
angle = float(input("Enter the angle (in degrees) of the sector: "))
angle_radians = math.radians(angle)  # Convert angle to radians
print("Area of the sector:", sector_area(radius, angle_radians))