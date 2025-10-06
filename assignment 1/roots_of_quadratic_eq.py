# roots of quadratic eq
a = float(input('enter value for coefficient a : '))
b = float(input('enter value for coefficient b : '))
c = float(input('enter value for coefficient c : '))

QE = (-b + (b**2 - 4*a*c)**0.5) / (2*a) 
QE1 = (-b - (b**2 - 4*a*c)**0.5) / (2*a) 

print(f'roots of quadratic eqs are : {QE} or {QE1}')