transactions: tuple = ('trans-001', 20000, 'Friday', '10:56AM' , {'bank_name':'mehwish_bank'})
print(transactions)
print(type(transactions))

# transactions[0] = 'trans-002' // This will cause an error
# print(transactions)

print(transactions[2])

# How many times a value has occured
assets = ('HP Elitebook', 'Dell Espiron', 'Asus', 'HP Elitebook')
total = assets.count('HP Elitebook')
print(total)

occurence_place = assets.index('HP Elitebook')
print(occurence_place)

### Control Flow - Conditions ###

admin = False
if admin:
    print('Admin Verified')

else:
    print('Admin Not Verified')

# Unique Emails
registered_email = {'ali@gmail.com', 'mehwish@yahoo.com'}
current_val = 'hussain@gmail.com'

if current_val in registered_email:
    print('Email already Exists') 
else:
    print('Email Available')


available_items = ['juice', 'chips', 'chocolate']
customer_searches = ['washing powder', 'mobile', 'chocolate']

if customer_searches not in available_items:
    print('Out of stock')
else:
    print('In Stock')

# AND - OR operator
if 10 > 9 and 2 < 3 and 10 > 20:
    print(True)
else:
    print(False)


print('OR Operators')

if 10 != 9 or 2 < 3 or 'ali' == 'ali':
    print(True)
else:
    print(False)

if 10 == 9 or 2 > 3 or 'ali' != 'ali':
    print(True)
else:
    print(False)