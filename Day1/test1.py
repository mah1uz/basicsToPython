'''❤️this is the function fpr printing a string or something'''

# print("Hello, World!")
# print("this is a test.")
# print("This is another attempt of printing a sententce.")

'''❤️this is to see the version of python being used'''

# import sys
# print(sys.version)  

'''❤️ Indentation in pYTHON'''

# if 11>12:  #1st block of if condition
#  print("78 is greater than 12")
# else:      # 2nd block of the if condition
#  print("12 is greater than 11")


# if 5 > 2:
#     print("Inside the if block")
#     print("Still inside")
# print("Now we’re OUTSIDE the if block")

'''❤️ Variables in Python and printing principles'''


# x="Hello, World!"
# print(x)
# x=55
# print("Hello, "+str(x)+ " World!")
# print ("hello vai......", end="")
# print( " we are in the same line haha")
# print("I am " + str(35) + " years old.")
# print("I am " ,35, " years old.")


'''❤️Comment out in Python'''

 
 # This is a single-line comment

'''This is a multi-line comment                     
that spans multiple lines.'''   

"""This is another multi-line comment
that also spans multiple lines."""

"""in vs code i can use ctrl + / to comment or uncomment a line or a block of code"""

"""Data Types printing and checking"""
# x=12
# print(type(x))

"""camelCase"""
# myVariableName= "John"

'''Many declarations in one line'''

# x,y,a = 11, "Banana", 'whythough'
# print(x,y, a, sep='IKNOWYOU')
# print(x,y, a, sep='')

# x=z=A= 'ORANGE'
# print(z,A,z, sep='***')


# x='myWorld'
# y=45
# print(str(x)+ str(y), sep=' hii')
# print(x,y, sep='****')

'''❤️ Global Variables '''

# x="nowYouSeeMe"
# y=22

# def myFunc():
#     print("These are the varibales:" , x,y, sep='*')
   
# print("Outside the function:", x,y, sep='-')
# myFunc()    



# x="good"

# def myFunction():
#    x= "best"
#    print("My first initializated var:" +x )
   
# myFunction()
# print('this is my second initialization: '+ x)



# global x
# x=69
# p=12
# def myFunction():
#     global p
#     p= 'NowYouDont'
#     print("Inside the function:", p, x)
# myFunction()
# p=69
# print("Outside the function:", p, x)

'''❤️ Data Types in Python'''

'''
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType
'''



# x = range(6)
# print(x)
# for n in x:
#   print(n)
# print(type(x))]



# x = 35e3
# y = 12E4
# z = 2e1

# print(type(x))
# print(type(y))
# print(type(z))
# print(z)



# import random
# print(random.randrange(1,10))
# print(random.randint(1,10))
# print(random.randfloat(0,100))


a='''this is a test of a string that is a sentence'''
print(a)
print(type(a))