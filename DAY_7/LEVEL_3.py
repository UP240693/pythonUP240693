age = [22, 19, 24, 25, 26, 24, 25, 24]

print(len(set(age)) < len(age))  # len of list is bigger

'''
List is a non-homogeneous data structure which stores the elements in single row and multiple rows and columns
Tuple is also a non-homogeneous data structure which stores single row and multiple rows and columns
Set data structure is also non-homogeneous data structure but stores in single row
'''

string = 'I am a teacher and I love to inspire and teach people.'
print(len(set(string.split())))