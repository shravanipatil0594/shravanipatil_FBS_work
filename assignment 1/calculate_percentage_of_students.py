# calculate percentage of students
name = input('enter you name : ')
maths = float(input('enter marks for maths : '))
eng = float(input('enter marks for english : '))
sci = float(input('enter marks for science : '))
hist = float(input('enter marks for history : '))
hindi = float(input('enter marks for hindi : '))

sum = maths+eng+sci+hist+hindi
per = (sum / 500) * 100

print(f'percentage of {name} is : {per}')