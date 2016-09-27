Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:01:18) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 2+2
4
>>> a=2
>>> b=8
>>> a+b
10
>>> a*b
16
>>> (5*a)+(8/b)
11.0
>>> 8%5
3
>>> 8/a
4.0
>>> float 8/a
SyntaxError: invalid syntax
>>> 8/a
4.0
>>> 8//a
4
>>> 9/a
4.5
>>> 9//a
4
>>> 9%a
1
>>> 18*8+8
152
>>> 5*3+2
17
>>> (5*3)+2
17
>>> 2**3
8
>>> 64*64
4096
>>> 8**4
4096
>>> 4096*4096
16777216
>>> 8**8
16777216
>>> -8**8
-16777216
>>> (-8)**8
16777216
>>> #aktina kouklou
>>> radius=10
>>> area=3.17*radius**2
>>> print("the area of kuklos with radius", radius, "is counting", area)
the area of kuklos with radius 10 is counting 317.0
>>> radius=20
>>> print("the area of kuklos with radius", radius, "is counting", area)
the area of kuklos with radius 20 is counting 317.0
>>> radius=10
>>> area=3.14 * radius**2
>>> print("the area of kuklos with radius", radius, "is counting", area)
the area of kuklos with radius 10 is counting 314.0
>>> radius=20
>>> area=3.14*radius**2
>>> print("the area of kuklos with radius", radius, "is counting", area)
the area of kuklos with radius 20 is counting 1256.0
>>> a=10
>>> b=20
>>> print("(a=",a,")",("b=",b,")")
      b=a
      
SyntaxError: invalid syntax
>>> print("(a=",a,")","(b=",b,")")
(a= 10 ) (b= 20 )
>>> b=a
>>> a=b
>>> print("(a=",a,")","(b=",b,")")
(a= 10 ) (b= 10 )
>>> t=a
>>> a=b
>>> b=t
>>> print("(a=",a,")","(b=",b,")")
(a= 10 ) (b= 10 )
>>> a=10
>>> b=20
>>> print("(a=",a,")","(b=",b,")")
(a= 10 ) (b= 20 )
>>> t=a
>>> a=b
>>> b=t
>>> print("(a=",a,")","(b=",b,")")
(a= 20 ) (b= 10 )
>>> a=10
>>> b=20
>>> print("(a=",a,")","(b=",b,")")
(a= 10 ) (b= 20 )
>>> b,a=a,b
>>> print("(a=",a,")","(b=",b,")")
(a= 20 ) (b= 10 )
>>> 3*3.75/1.5
7.5
>>> 7.0/2
3.5
>>> 8**15
35184372088832
>>> a,b=0,1
>>> while b<10
SyntaxError: invalid syntax
>>> while b<10:
	print(b)
	a,b=b,a+b

	
1
1
2
3
5
8
>>> i=256**2
>>> print('the value of i is', i)
the value of i is 65536
>>> a,b=0,1
>>> while b<1000:
	print(b,end=',')
	a,b=b,a+b

	
1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,
>>> for test_number in range(1,10000)
SyntaxError: invalid syntax
>>> for test_number in range(1,10000):
	sum=0
	for i in range(1,test_number):
		if test_number%1==0
		
SyntaxError: invalid syntax
>>> for test_number in range(1,10000):
	sum=0
	for i in range(1,test_number):
		if test_number%1==0:
			sum +=i
	if sum==test_number:
		print(test_numeber,"is perfect number")

		
Traceback (most recent call last):
  File "<pyshell#95>", line 7, in <module>
    print(test_numeber,"is perfect number")
NameError: name 'test_numeber' is not defined
>>> for test_number in range(1,10000):
	sum=0
	for i in range(1,test_number):
		if test_number%i==0:
			sum +=i
	if sum==test_number:
		print(test_numeber,"is perfect number")

		
Traceback (most recent call last):
  File "<pyshell#98>", line 7, in <module>
    print(test_numeber,"is perfect number")
NameError: name 'test_numeber' is not defined
>>> for test_number in range(1,10000):
	sum=0
	for i in range(1,test_number):
		if test_number%i==0:
			sum +=i
		if sum==test_number:
		print(test_numeber,"is perfect number")
		
SyntaxError: expected an indented block
>>> for test_number in range(1,10000)
SyntaxError: invalid syntax
>>> for test_number in range(1,10000):
	sum=0
	for i in range(1, test_number):
		if test_number % i == 0:
			sum + = i
			
SyntaxError: invalid syntax
>>> for test_number in range(1,10000):
	sum=0
	for i in range(1, test_number):
		if test_number % i == 0:
			sum += i
	if sum == test_number:
		print(test_number, "is a perfect number")

		
6 is a perfect number
28 is a perfect number
496 is a perfect number
8128 is a perfect number
>>> i=0
>>> while i<=10:
	if i%2 == 0:
		print(i, "is a multiple of 2")
	elif i%3 ==0:
		print(i,"is a multiple of 3)
		      
SyntaxError: EOL while scanning string literal
>>> i=0
>>> while i<=10:
	if i%2 == 0:
		print(i, "is a multiple of 2")
	elif i%3 ==0:
		print(i,"is a multiple of 3")
		
SyntaxError: multiple statements found while compiling a single statement
>>> i=0
>>> while i<=10:
	if i % 2 ==0:
		print(i, "is a multiple of 2")
	elif i % 3 ==0:
		print(i, "is a multiple of 3")
	else:
		print(i, "is not a multiple of 3 nor 3")
	i += 1

	
0 is a multiple of 2
1 is not a multiple of 3 nor 3
2 is a multiple of 2
3 is a multiple of 3
4 is a multiple of 2
5 is not a multiple of 3 nor 3
6 is a multiple of 2
7 is not a multiple of 3 nor 3
8 is a multiple of 2
9 is a multiple of 3
10 is a multiple of 2
>>> 
