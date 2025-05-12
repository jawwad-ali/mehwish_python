firstName: str = 'Ali'
secondName: str = 'Jawwad'
age: int = 24
isMarried: bool = False

print(firstName)
print(secondName)

print(type(firstName))
print(type(isMarried))

age = 21
print(age)

full_name: str = firstName + " " + secondName + "and my age is " + str(age)
print(full_name)

bio: str = f"My name is {firstName} {secondName} and my age is {age}"
print(type(bio))

number_1: int = 20
number_2: int = 10
print(number_1 // number_2)