# convert days into yrs and months
days = float(input('enter days : '))

years = days // 365
months = days % 365
weeks = days // 7
days = days % 7

print(f'total number of years are : {years}')
print(f'total number of months are : {months}')
print(f'total number of weeks are : {weeks}')
print(f'total number of days are : {days}')