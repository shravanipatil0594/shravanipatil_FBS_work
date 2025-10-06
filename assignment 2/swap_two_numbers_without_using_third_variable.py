# swap two numbers without using third variable
x = 10
y = 20

print(f'Before swapping x is : {x}, & y is : {y}')

##x = x+y #30

##y = x-y #30-20=10 ; y=10

##x = x-y #30-10=20

x,y=y,x

print(f'after swapping x is : {x}, & y is : {y}')