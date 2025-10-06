# interior and exterior wall 
int_wall = float(input('enter sq feet of interior wall : '))
ext_wall = float(input('enter sq feet of exterior wall : '))
cost = float(input('enter cost : '))

int_cost = int_wall * cost
ext_cost = ext_wall * cost

print(f'cost of interior wall is : {int_cost}')
print(f'cost of exterior wall is : {ext_cost}')