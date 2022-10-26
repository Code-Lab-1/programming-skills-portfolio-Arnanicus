rivers = {
'Yangzte' : 'China',
'Nile' : 'Egypt',
'Tigris' : 'Mesopotamia',
'Mississippi': 'the United States of America'
}
for river, country in rivers.items():
    print(river.title() + " is in " + country.title())

print("\nThe rivers in this dictionary are: ")
for river in rivers.keys():
    print("The "+ river.title() + " River")

print("\nThe countries in this dictionary are: ")
for country in rivers.values():
    print("The country of " + country.title())