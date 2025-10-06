# digit separation and reverse numbers str
num = 123
temp = num

print(f"before digit seperation {num}")

d1 = temp % 10
temp = temp // 10

d2 = temp % 10
temp = temp // 10

d3 = temp % 10
temp = temp // 10

temp = d1+100+d2+10+d3
print(f"after digit seperation {temp}")

