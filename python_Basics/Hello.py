print("Hello Python\n")
# \n --> use to change the line
print('Python is a popular programming language.\n It was created by Guido van Rossum, and released in 1991.\n')


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

print('\t"What is the use of python"\n')

print("'web development (server-side),\nsoftware development,\nmathematics,\nsystem scripting.'")

'''         Python Indentation                           

                    Indentation refers to the spaces at the beginning of a code line.

Where in other programming languages the indentation in code is for readability only, the indentation in Python is very important.

---------------->Python uses indentation to indicate a block of code.

    if 5>3: # this will not work if you give space to it
    print('greater')
    '''
if 5>3: 
 print('greater')