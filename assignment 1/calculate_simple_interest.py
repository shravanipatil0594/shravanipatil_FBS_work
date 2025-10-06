# calculate simple interest
principal_amt = float(input('enter value for principal amount : '))
rate = float(input('enter value for rate : '))
time = float(input('enter value for time : '))

simp_int = principal_amt*rate*time / 100

print(f"simple interest is {simp_int}")
