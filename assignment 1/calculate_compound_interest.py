# calculate compound interest
principal_amt = int(input('enter value for principal amount : '))
rate = int(input('enter value for rate : '))
time = int(input('enter value for time : '))

A = principal_amt * (1+(rate / 100))**time
CI= A - principal_amt

print(f'compound interest is {CI}')