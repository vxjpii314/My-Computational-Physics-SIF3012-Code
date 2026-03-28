#Approximating pi value using Archimedes' method .
# The range is from 0 to N. This means the 1 for 3 sides, 2 for 6 sides, 3 for 12 sides, ... N for n = 3/2*(2^N) sides !
import math
n = float(6)
y = float(1)

N = int(input("Type a number to end the range: "))
for i in range(0, N):

    x = math.sqrt(1 - pow(y/2,2))
    y_n = math.sqrt(pow((1-x),2) + pow(y/2,2))
    tot = float(n * y)
    Pi = tot/2
    print(Pi)
    y = y_n
    n = n*2.0 # The final pi value displayed at the last line of output .
"""
Explanation : 
The code is built to approximate the value of pi using Archimedes' method. The method starts with a hexagon (6 sided polygon). Pi is given by
the ratio between circumference and diameter of the circle. The perimeter(3 sides) of the 'half polygon' can be used to approximate the circumference 
of the circle. What I did first was to find the iteration formula by hand. Each side of the polygon is divided by 2 to form a polygon with twice number of sides. 
We keep doubling the side of these polygons. Theoretically, when n->inf, the polygon sides will approach the circumference of the circle, and that's how the method works .
"""
