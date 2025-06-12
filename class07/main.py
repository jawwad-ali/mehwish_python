# Positional Arguments
# Default Parameters
# *args
# **kwargs

# Indifinite number of Arguments (*args)
def wallet(color, *kuch_bhi):
    print(color, kuch_bhi)

wallet('red', 'currency', 'NIC', 'Debit Card')

def citizen( **kwargs ):
    print(type(kwargs))
    print(kwargs)
    print(kwargs['name'])

citizen( name = 'Mehwish', age = 23, id_card = 423019242093, passport_number = 838831 )


# Loops
# For Loop (when you have an ending point)
# While Loop (Jab tk ek condition false nahi hojati/ true rehti hai)


for i in range(50, 0, -3):
    print(i)

for k in range(0, 50, 3):
    print(k)

cart = [
    {'name': 'shoes', 'price': 100},
    {'name': 'wallet', 'price': 140},
    {'name': 'mobile', 'price': 1000},
    {'name': 'toy', 'price': 250},
]

total: int = 0
for kharcha in cart:
    #       0     +   100 = 1000
    #     = 100   +   140 = 240
    #     = 240   +   1000 = 1240
    total = total + kharcha['price']
print("The Total bill amount is <==>",total)



# While Loop
total = 0
while True:
    price_input: str = input('Enter your price')

    if price_input == 'done':
        break

    if price_input.isnumeric():
        total += int(price_input)
        print(f'total Price is {total}')





