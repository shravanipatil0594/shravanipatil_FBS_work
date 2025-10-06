# selling price
cp = float(input('enter cost price of book : '))
dis = float(input('enter discount on books : '))

sp = cp - (dis*cp/100)

print(f'selling price is : {sp}rs')