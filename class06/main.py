# Basic Function
def greet():
    print("Good Evening Ali Jawwad!")

greet()

# Function Parameters
def welcome(name: str):
    print(f'Welcome {name}')

welcome('Ali')
welcome('mehwish')

def getUserInfo(name: str, email: str, age: int):
    print(name, email, age)

getUserInfo('Kohli', 'kohli@gmail.com', 36)

# Return Statement
def add(num1, num2):
    # print(num1 + num2)
    return num1 + num2

result = add(10, 21)
print(result)


def calc(num1, num2, operation):
    if operation == "+":
       return num1 +  num2

    elif operation == "-":
        return num1 - num2


result = calc(12 , 33 , "+")
print(result)


# Indifinite number of Arguments (*args)
def wallet(color, *kuch_bhi):
    print(color, kuch_bhi)

wallet('red', 'currency')

def fileUpload(*files):
    print(files)

fileUpload('one.png', 'two.ppt', 'three.xlsx')


# Default Parameters
def website_theme(color:str = 'light'):
    print(color)
website_theme()
website_theme('dark')