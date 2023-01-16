from sympy.abc import x,y
from sympy import integrate, cos, sin, pi, sqrt

def doub_intg(integrand,x1,x2,y1,y2,wrt):
    if wrt == "x":
        I1 = integrate(integrand,(x,x1,x2),(y,y1,y2))
        print(I1)
    elif wrt == "y":
        I1 = integrate(integrand,(y,y1,y2),(x,x1,x2))
        print(I1)
doub_intg(x+y,0,1,0,2,"y")
doub_intg(cos(x)*sin(x),0,pi/6,0,pi/3,"x")
doub_intg(x*y**2,1,2,0,x,"y")
doub_intg(1,0,3,0,sqrt(9-x**2),"y")
doub_intg(x**2+y,0,1,x,x**2,"y")
