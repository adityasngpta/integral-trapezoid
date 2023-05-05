# Integral Calculator with Trapezoids
By Aditya Sengupta

This project is a continuation of my prior project, Integral Calculator.
However, instead of using rectangles, this code uses trapezoids in 2 different methods to calculate the area under the curve.

Method 1
Calculates the rectangles as before, but adds triangles on top of each rectangle. A rectangle plus a triangle on top is a trapezoid.
The base of the triangle is the width of the rectangle, and the height of the triangle is the derivative of f(x) at the ith rectangle value times the width of the rectangle.
For the function, y = x^2, the trapezoid method at n = 1,000 is more effective than the rectangle method at 100,000.

Method 2
This method involves finding f(x_i) and f(x_i+1) and averaging them to find the bases of the trapezoid, then multiplying by the width to get the area.
With the Method 1, it was an add on to a left hand sum so we knew the area would always be a little less than the area of he curve.
Method 2 cannot guarantee if the area will be greater or less than the area of the curve.
