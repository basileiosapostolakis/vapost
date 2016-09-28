import math
a=input("Enter number of a:")
b=input("Enter number of b:")
c=input("Enter number of c:")
i=(b**2)-(4*a*c)
if i<0 print("no real-valued solution")
else x=(-b+-math.sqrt(i))/(2*a)
