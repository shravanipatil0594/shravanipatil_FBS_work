# salary of employee
basic_salary = float(input('enter basis salary for employees : '))
da = 10
ta = 12
hra = 15

da1 = 0.10 * basic_salary
ta1 = 0.12 * basic_salary
hra1 = 0.15 * basic_salary

total_salary = basic_salary + da1 + ta1 + hra1

print(f'dearness allowance of an employee is : {da}rs')
print(f'travel allowance of an employee is : {ta}rs')
print(f'house rent allowance of an employee is : {hra}rs')
print(f'total salary of an employee is : {total_salary}rs')