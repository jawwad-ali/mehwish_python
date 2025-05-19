students: dict = {
    "name": "Ali Jawwad",
    "age": 24,
    "email": 'ali@gmail.com',
}

print(students)
print(students['name'])
print(students['age'])
print(students['email'])
# print(students['favColor']) Key Error

# Adding a new key MANUALLY
students['subjects'] = 'Maths'
print(students)

# Second way of adding a new KEY
students.update({'attendance' : '80%'})
print(students)

students.update({'name': 'Jawwad Ali'})
print(students)


# Deleting a KEY
# pop, del

students.pop('age')
print(students)

del students['name']
print(students)

# Nested Dictionary
year = {
    "months": {
        'first_month' : 'January',
        'second_month': 'Febuary'
    },
    'holy_months': ['Moharram' , 'Ramzan', 'Rabi-ul-Awwal']
}
print(year['months']['first_month'])
print(year['holy_months'][1])


# List with Dictionary
multiple_students = [
    {
        'name': 'Mehwish',
        'email': 'mehwish@gmail.com',
        'sub': ['maths' , 'eng'],
        'attendance': '100%'
    },
    {
        'name': 'Ali',
        'email': 'ali@gmail.com',
        'sub': ['science' , 'urdu'],
        'attendance': '50%'
    }
]
print(multiple_students[1]['sub'][1])



# Dictionary Methods
# Dictionary methods
print(students.keys())
print(students.values())
print(students.items())
