pet = []
petanimal = {
'Name' : "Mike",
'Age' : '2',
'Animal' : "Dog",
}
pet.append(petanimal)
petanimal = {
'Name' : "Boba",
'Age' : '1',
'Animal' : "Cat",
}
pet.append(petanimal)
petanimal = {
'Name' : "Hubert",
'Age' : '300',
'Animal' : "Dragon",
}
pet.append(petanimal)

for petanimal in pet:
    print("\nThis is some information about " + petanimal['Name'].title() + ":")
    for key, value in petanimal.items():
        print("The " + key + " is " + str(value) + "!")