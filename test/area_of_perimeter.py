# area of perimeter
length = float(input('enter value for len : '))
breadth = float(input('enter value for B : '))
radius = float(input('enter value for r : '))

rect_area = length * breadth 
# rect_peri = 2(length + width)
semicircle = (3.14*radius) + (2*radius)

area_of_peri = rect_area + semicircle

print(f'area of perimeter is {area_of_peri}')

