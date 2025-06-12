months: set = {'January', 'Febuary', 'March', 'January'}

print(months)

my_score: set = {1, 100, 21, 34 , 100}
print(my_score)

# print(my_score[0]) // This will throw an error

# Adding items in set
months.add('April')
print(months)


fruits = {'apple', 'mango' , 'orange'}
season = {'summer', 'winter', 'spring'}
price = [109, 1340, 348]


fruits.update(season, price)
print(fruits)


# Union
laugh_react = {'ali' , 'haseeb' , 'hussain'}
wow_react = {'mehwish' , 'mariam' , 'nimra'}

all_reactions = set()

all_reactions = all_reactions.union(laugh_react , wow_react)
print(all_reactions)

# Intersection
mehwish_FL = {'abc' , '123' , 'xyz'}
ali_FL = {'samsung', 'abc', 'apple', 'xyz'}

mutual_friends = ali_FL.intersection(mehwish_FL)

print(mutual_friends)
