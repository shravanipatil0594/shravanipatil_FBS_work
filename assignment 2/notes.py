# notes
notes = int(input('enter amount : '))

num2000 = notes // 2000
print(num2000)
amt1 = notes % 2000

num500 = amt1 // 500
print(num500)
amt2 = notes % 500

num200 = amt2 // 200
print(num200)
amt3 = notes % 200

num100 = amt3 // 100
print(num100)
amt4 = notes % 100

num50 = amt4 // 50
print(num50)
amt5 = notes % 50

num20 = amt5 // 20
print(num20)
amt6 = notes % 20

num10 = amt6 // 10
print(num10)
amt7 = notes % 10

total_notes = num2000+num500+num200+num100+num50+num20+num10
print("total notes :",(total_notes))