#print("Hello Python\n")
# \n --> use to change the line
#print('Python is a popular programming language.\n It was created by Guido van Rossum, and released in 1991.\n')


#\t --> \t represents a tab character. It's used to create horizontal space in your output.
'''             How to print in double quotes

    1) we ca use both double quotes (" ")  or single quotes (' ') to print a statement.
    2)  print(' 'Raj' '); is gives you error, Here python will confused from where  quotes starts.because both quotes are same.
                ---------- Two Ways to do this--------------

                1)          using Escape:
                    Escape the single quotes inside the string using backslashes (\):
                    eg: print(' \'Raj\' ').
                2) Use double quotes to wrap the string, so single quotes can be used directly inside:
                  eg: print(" 'Raj' ") , print('"Raj"')---both works fine.


'''

#print('\t"What is the use of python"\n')

#print("'web development (server-side),\nsoftware development,\nmathematics,\nsystem scripting.'")

'''         Python Indentation                           

                    Indentation refers to the spaces at the beginning of a code line.

Where in other programming languages the indentation in code is for readability only, the indentation in Python is very important.

---------------->Python uses indentation to indicate a block of code.

    if 5>3: # this will not work if you give space to it
    print('greater')
    '''
"""if 5>3: 
 print('greater')"""

'''------------------------Variables-------------------------------
  -->variable are containers for storing data values.
   to declare variable in python no need to declare data type.


   
'''
        # casting
"""x=str(3)  #'3'
y=int(3) #3
z=float(3) #3.0"""

# get the data type of variable with type()function
"""x=5
y="john"
print(type(x))
print(type3(y))"""

#String variables can be declared either by using single or double quotes
#python is case sensitive

'''

                              Variable Names


A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). 
    Rules for Python variables:
A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
A variable name cannot be any of the Python keywords.'''

'''Many Values to Multiple Variables'''

# x, y, z = "Orange", "Banana", "Cherry"
# print(x)
# print(y)
# print(z)

''' One Value to Multiple Variables'''
# x = y = z = "Orange"
# print(x)
# print(y)
# print(z) 


"""Unpack a Collection
If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking."""
# fruits=["apple","banana","cherry"]
# x,y,z=fruits
# print(x)
# print(y)
# print(z)
'''In the print() function, you output multiple variables, separated by a comma'''

# x="python"
# y="is"
# z="awesome"
# print(x,y,z)
'''space character after "Python " and "is ", without them the result would be "Pythonisawesome".'''
# x=5
# y=10
# print(x+y)

'''In the print() function, when you try to combine a string and a number with the + operator, Python will give you an error:
x=5
y=""john
print(x+y) ------------> gives you error
'''
'''separate them with commas, which even support different data types:'''

# x = 5
# y = "John"
# print(x, y)