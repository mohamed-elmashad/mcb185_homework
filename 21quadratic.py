# authors: Mo, Aidan
import math

def quadratic(a, b, c):
	discriminant = (b**2) - (4*a*c)
	sqrt_discriminant = math.sqrt(abs(discriminant))

	if discriminant > 0:
		return ((-b + sqrt_discriminant)/(2 * a)), ((-b - sqrt_discriminant)/(2 * a))
	elif discriminant == 0: 
		return (-b / (2 * a)), (-b / (2 * a))
	else:
		print("Complex root, cannot return values")
        
print("a = 6, b = -11, c = -30")
print(quadratic(6, -11, -30))

print("a = 1, b = -4, c = 4")
print(quadratic(1, -4, 4))

print("a = 1, b = 1, c = 1")
print(quadratic(1, 1, 1))