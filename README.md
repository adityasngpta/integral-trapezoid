# Integral Calculator with Trapezoids
By Aditya Sengupta

This project is a continuation of my prior project, Integral Calculator.
However, instead of using rectangles, this code uses trapezoids to calculate the area under the curve.
It is the same as rectangles, but with triangles on top of each rectangle. A rectangle plus a triangle on top is a trapezoid.
The base of the triangle is the width of the rectangle, and the height of the triangle is the derivative of f(x) at the ith rectangle value times the width of the rectangle.
For the function, y = x^2, the trapezoid method at n = 1,000 is more effective than the rectangle method at 100,000.
