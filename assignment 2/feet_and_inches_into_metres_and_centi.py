# feet and inches into meters and centi
feet = float(input('enter feets : '))
inches = float(input('enter inches : '))

meter = feet * 0.3048
meter1 = inches * 0.0254

centi = feet * 30.48
centi1 = inches * 2.5

print(f'feet to meters : {meter}m')
print(f'inches to meters : {meter1}m')

print(f'feet to centimeters : {centi}cm')
print(f'inches to centimeters : {centi1}cm')



