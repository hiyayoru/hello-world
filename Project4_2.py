sphereRadius = float(input("Please enter the radius of a sphere: "))
pi = 3.141592653589793

sphereDiameter = sphereRadius * 2
sphereCircumference = 2 * pi*sphereRadius
sphereSurfaceArea = 4 * pi * sphereRadius**2
sphereVolume = 4/3 * pi * sphereRadius**3

print("The Diameter of the Sphere is: ", sphereDiameter)
print("The Circumference of the Sphere is: ", sphereCircumference)
print("The Surface Area of the Sphere is: ", sphereSurfaceArea)
print("The Volume of the Sphere is: ", sphereVolume)

input("Press enter to close")
