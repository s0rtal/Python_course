#monte carlo pi approximation
import random
number_of_points = 100000
number_of_points_in = 0
radius = 10000000
i = 0
while i < number_of_points:
    num1 = random.randint(-radius, radius)
    num2 = random.randint(-radius, radius)
    num1 *= num1
    num2 *= num2
    if num2 + num1 <= radius*radius:
        number_of_points_in += 1
    i += 1
pi = 4*number_of_points_in/number_of_points
print(pi)