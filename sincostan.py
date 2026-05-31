import math

# Input angle in degrees
angle = float(input("Enter angle in degrees: "))

# Convert degrees to radians
radian = math.radians(angle)

# Calculate trigonometric values
sin_value = math.sin(radian)
cos_value = math.cos(radian)
tan_value = math.tan(radian)

# Display results
print("sin(", angle, ") =", sin_value)
print("cos(", angle, ") =", cos_value)
print("tan(", angle, ") =", tan_value)