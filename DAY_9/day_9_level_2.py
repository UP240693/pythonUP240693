# Level 2
# 1
score = int(input("Enter score: "))

grades = {}
for i in range(90, 101):
    grades[i] = 'A'
for i in range(70, 90):
    grades[i] = 'B'
for i in range(60, 70):
    grades[i] = 'C'
for i in range(50, 60):
    grades[i] = 'D'
for i in range(0, 50):
    grades[i] = 'F'

print("Grade:", grades[score])

# 2
month = input('Enter month: ').title()
if month in ["September", "October", "November"]:
    print("Autumn")
if month in ["December", "January", "February"]:
    print("Winter")
if month in ["March", "April", "May"]:
    print("Spring")
else:
    print("Summer")

# 3
fruits = ['banana', 'orange', 'mango', 'lemon']
fruit = input('Enter fruit: ')
print('That fruit already exists in the list' if fruit in fruits else fruits.append(fruit))
print(fruits)
