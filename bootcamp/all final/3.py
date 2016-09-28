import math
a=input("Enter the a side of the triangle:")
b=input("Enter the b side of the triangle:")
c=input("Enter the a side of the triangle:")
x=(int(a)+int(b)+int(c))
y=(-int(a)+int(b)+int(c))
z=(int(a)-int(b)+int(c))
e=(int(a)+int(b)-int(c))
w=x*y*z*e
m=math.sqrt(w)
A=(1/4)*m
print( "Calculation of the area of a triange is:", A)

