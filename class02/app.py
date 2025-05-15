# Arrays - LISTS - Data of Same Context

months: list[str] = ['January', 'Feb' , 'March']
phone_book: list[int] = [123, 23489, 982473]

print(months)
print(type(months))

print( months[2]  )

# Negative Indexing
print( months[-2] )

blogs = ['blog1' , 'blog2' , 'blog3' , 'blog 4' , 'blog 5' , 'blog 6' , 'blog 7' , 
         'blog 8' , 'blog 9' , 'blog 10' , 'blog 11' , 'blog 12', 
         'blog 13' , 'blog 14']

print('Slicing with Positive Indexing', blogs[ 1 : 5 ] )

print('Slicing with Negative Indexing', blogs[ -6 : -1] )

print('Slicing with One Index', blogs[-6: ])


# Append
months.append('April')
print("Appended Months ",months)

months.insert(1 , 'Dec')
print(months)


# Removing elements from the list
months.pop()
print(months)

whatsapp_chats = ['abcd' , 'efg' , 'Comedy Group' , 'akdnlak' , 'aksdaslkn' , 'Comedy Group']
print(whatsapp_chats)
whatsapp_chats.remove('Comedy Group')
print(whatsapp_chats)


nested_list: list[str] = ['laptop' , 'mobile' , 'computer' , 
['nested item 1', 'nested item 2', 'nested item 3']  ] # mypy will throw an error


nested_list: list[list[str]] = ['laptop' , 'mobile' , 'computer' , ['nested item 1', 'nested item 2', 'nested item 3']  ]
# print( nested_list[3][1]  )

print( nested_list[3][0] )