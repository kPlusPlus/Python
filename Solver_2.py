# importing library sympy
from sympy import symbols, Eq, solve

# defining symbols used in equations
# or unknown variables
x, y, z = symbols('x,y,z')
a, b, c = symbols('a,b,c')

# defining equations
#eq1 = Eq((x+y+z), 1)
eq1 = Eq((a+a+a), 30) # a + a + a = 30
print("Equation 1:")
print(eq1)

#eq2 = Eq((x-y+2*z), 1)
eq2 = Eq((b+b+a), 20) # b + b + a = 20
print("Equation 2")
print(eq2)

eq3 = Eq((c+c+b), 13) # c + c + b = 13
print("Equation 3")
print(eq3)



# solving the equation and printing the
# value of unknown variables
print("Values of 3 unknown variable are as follows:")
#print(solve((eq1, eq2, eq3), (x, y, z)))
print(solve((eq1, eq2, eq3), (a, b, c)))
