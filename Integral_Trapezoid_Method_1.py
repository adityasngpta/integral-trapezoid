# Integral Calculator Using N Trapezoids - Method 1
# By Aditya Sengupta

'''
This project is a continuation of my prior project, Integral Calculator.
However, instead of using rectangles, this code uses trapezoids to calculate the area under the curve.
It is the same as rectangles, but with triangles on top of each rectangle. A rectangle plus a triangle on top is a trapezoid.
The base of the triangle is the width of the rectangle, and the height of the triangle is the derivative of f(x) at the ith rectangle value times the width of the rectangle.
For the function, y = x^2, the trapezoid method at n = 1,000 is more effective than the rectangle method at 100,000.
'''

# Variables
a = 0 # Lower bound of the integral
b = 1 # Upper bound of the integral
n = 1_000 # Number of Trapezoids to use

# The function to calculate the area under the curve for.
def f(x):
    return x**2

# Derivative of the function f(x)
def derivative(f, x):
    h = 1e-9 # a small value to calculate the limit
    fx = f(x)
    fx_plus_h = f(x + h)
    return (fx_plus_h - fx) / h


# Integral Function
def integral(a, b, n): # Taking the left hand Riemann sum and adding the triangles on top of each rectangle to make trapezoids.
    
    # Calculates the area under the curve f(x) from a to b using n trapezoids.

    area = 0 # Area under the curve

    width = (b-a)/n # Width of each rectangle

    def x_i(i): # Calculates the x value of the ith rectangle
        return a + i * width
    
    for i in range(n): # Calculates the area of each rectangle and adds it to the total area
        # Adding Rectangle
        area += width * f(x_i(i))
        # Adding Triangle
        triangle_height = derivative(f, x_i(i)) * width
        area += 0.5 * width * triangle_height
    return area

# Output
print("\nThe area of f(x) in the interval [", a, ",", b, "] is approximately", integral(0, 1, n), "using trapezoid method 1.\n")