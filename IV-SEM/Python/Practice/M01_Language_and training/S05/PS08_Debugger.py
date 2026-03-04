'''
Bug->Error
Finding and Fixing of Errors is called Debugging...
Types of Errors:
1. Syntax Error: Occurs when the code is not written in proper format missing colons, parentheses, indentation etc.
2. Logical Error: Occurs when the code is syntactically correct but the output is not as expected
3. Runtime Error: Occurs when the code is syntactically correct but an error occurs during execution

Debugging Techniques:
1. print()
2. Using of pdb module
3.try-Except block
4. Using IDE Debugger

pdb->Python Debugger
purpose:
1.pause the execution at certain point
2.inspect the variables
3.execute the code line by line
pdb commands:
    1.n->Toget the output in the next line
    p variable->To print the value of the variable
    c->To continue the execution until next breakpoint 
    l-->To see the code in the current function
    s->To step into the function(start)
    r->To step out of the current function(return)
    h->To see the list of pdb commands(help)
    q->To quit the debugger

 '''
'''try:
    a=int(input("Enter a number:"))
    print(10/a)
except ZeroDivisionError:
    print("Denominator should not be zero")
except ValueError:
    print("Invalid Input")
'''

import pdb
def add(a,b):
    pdb.set_trace()
    return a+b
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))    
print(add(a,b))
