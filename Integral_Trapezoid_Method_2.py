# Integral Calculator Using N Trapezoids - Method 2
# By Aditya Sengupta

'''
Based on the prior method of making a trapezoid using the rectangle and adding a right triangle on top with the hypotenuse slope being the derivative, there is an alternate method.
This method involves finding f(x_i) and f(x_i+1) and averaging them to find the height of the trapezoid, then multiplying by the base to get the area.
With the left hand sum using the trapezoids, we knew the area would always be a little less than the area of he curve.
This method cannot guarantee if the area will be greater or less than the area of the curve.
'''

# Variables
a = 0 # Lower bound of the integral
b = 1 # Upper bound of the integral
n = 1_000 # Number of Trapezoids to use

# The function to calculate the area under the curve for.
def f(x):
    return x**2

# Integral Function
def integral(a, b, n): # Taking essentially a blend of the left and right hand Riemann sum by turning the rectangle into a trapezoid
    
    # Calculates the area under the curve f(x) from a to b using n trapezoids.

    area = 0 # Area under the curve

    width = (b-a)/n # Width of each rectangle

    def x_i(i): # Calculates the x value of the ith rectangle
        return a + i * width
    
    for i in range(n): # Calculates the area of each trapezoid and adds it to the total area
        # Adding Rectangle
        area += width * (f(x_i(i)) + f(x_i(i+1)))/2 # Area of the trapezoid is the average of the two heights times the width

    return area

# Output
print("\nThe area of f(x) in the interval [", a, ",", b, "] is approximately", integral(0, 1, n), "using trapezoid method 2.\n")