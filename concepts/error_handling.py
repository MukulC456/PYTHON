'''
Error handling: When I have a problem with my code that is running and it's not something 
                I am going to be able to predict when I pushed my code out to production.
                For e.g. permissions issues, database changing, server being down, etc.
                Those things that happen in real world and we do not have control over.

Debugging: When I know that there is a problem with my code which is potentially giving me wrong answer
           and is crashing. And I know that I have done something incorrectly that's causing my code to 
           go sidways
'''
'''
3 types of error: Syntax error, runtime error, logical error

Syntax error: errors which occur before execution. The program refuses to start. Cuaght by compiler, IDE,
              or interpreter. Must be foxed in the code source.

Runtime error: errors which occur during execution(runtime). Impossible operations or bad inputs. The program
               starts but crashes later. Caught by system or user at execution.

Logical error: syntax is correct, code is running perfectly but we don't get the desired output. Let's understand
               by example below.
'''

# example for logical error
'''
# our messed up code
x = 206
y = 0

print("This is our messed up code.")
print(x/y)
'''
'''
# our clean-up code
x = 206
y = 0

try:
    print(x/y)
except ZeroDivisionError as e:
    print("Not allowed to divide by zero.")
else:
    print("Something else went wrong.")
finally:
    print("This is our clean-up code.")
'''