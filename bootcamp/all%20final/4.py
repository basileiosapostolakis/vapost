import math
a=input("Enter number of a:")
b=input("Enter number of b:")
c=input("Enter number of c:")
i=(int(b)**2)-(int(a)*int(c)*4)
if i<0:
    print("no real-valued solution value is:",i)
x1 =((-int(b))+(math.sqrt(i)))/(2*int(a))
x2 =((-int(b))-(math.sqrt(i)))/(2*int(a))
print("solution x1 is:",x1)
print("solution x2 is:",x2)
