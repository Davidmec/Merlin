from sympy import *
from sympy.plotting import plot3d
x = symbols('x')
y = x**2 + 1
plot(y)


x, y = symbols('x y')
f = 2 * x + 3 * y
plot3d(f)

summation = sum(2*i for i in range(1,6))
print(summation)

x = [1,4,6,2]
n = len(x)
print(sum(10*x[i] for i in range(0,n)))

# `Sum`, is different from a `sum``, `Sum` returns a function, that sums the results of the lambda, over the specified range, `sum` just adds all the numbers in the range together 
i, n = symbols('i n')
summation = Sum(2*i,(i,1,n))
print(summation)
# `.subs substitutes, a symbol for somthing`
print(summation.subs(n, 5).doit())
plot(summation)

x = symbols('x')
# SymPy will automatically simplify expressions for you
expr = x**2/x**5
print(expr)
plot(expr)

y = symbols('y')
f = log(8, y)
print(f)
plot(f)

# Compound interest and eulers numbers, the 
p, r, n, t = symbols('p r n t')
r = 1
p = 1000
plot3d( p * ( 1 + (r /n)) ** (n*t) )
## eulers number is the multiplicated, of the principle, as the period approaces infitiy
plot3d(( 1 + (r /n)) ** (n*t) )

## python the natural log, uses log, without an base specified
plot(log(symbols('y')))
plot(log(symbols('y'),2.71828169413))

#limits, numpy represents infinity as `oo` (two lowercase "o" (not zero 0) characters)
x = symbols('x')
f = 1/x
plot(f)
print(limit(f, x, oo))

#eulers is defined as lim((1+1/n)^n as n-> infinity
n = symbols('n')
f = (1+ 1/n)**n
plot(f)
print(limit(f, n, oo))
#sympi detects the above as eulers numbers and returns E, we use `evalf()` to get the decimal value
print(limit(f, n, oo).evalf())



######################## derivatives ##############################

#derivative (d/dx) is the slope of of f(x), at x, as measured by two infination close limit(1/x,oo) points, at x
x = symbols('x')
f = x ** 2
dx_f = diff(f)

# [python string interpolation](https://www.geeksforgeeks.org/python-string-interpolation/)
print(f"f:'{f}', dx(f):'{dx_f}'")
plot(f, dx_f) 

## partial derivaties

x,y = symbols('x y')
f = 2*x**3 + 3*y**3
dx_f = diff(f,x)
dy_f = diff(f,y)
print(f"dx_f:'{dx_f}', dy_f:'{dy_f}'")
plot3d(f, dx_f, dy_f)


#### chain rule ###
# dz_x == dz_y * dy_x
x, y = symbols('x y')
_y = x ** 2 + 1
z = y**3 -1

dy_dx = diff(_y)
dz_dy = diff(z)
dz_dx_chain = (dy_dx * dz_dy).subs(y,_y)
dz_dx_no_chain = (diff(z.subs(y,_y)))
print(f"x: {x}, y: {y}, _: {_y}, z: {x}, dy_dx:{dy_dx}, dz_dy:{dz_dy},  dz_dx_chain:{dz_dx_chain}, dz_dx_no_chain:{dz_dx_no_chain}")
plot3d(_y,z,dy_dx,dz_dy)
